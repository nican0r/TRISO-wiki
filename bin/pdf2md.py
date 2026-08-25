#!/usr/bin/env python3
"""PDF -> markdown converter for the LLM Wiki. No network, no ML deps.

Usage:  pdf2md.py <in.pdf> <out_dir> [--single-col | --two-col]

Emits:  <out_dir>/<slug>.md
        <out_dir>/figures/<slug>-pNN.png   (rendered pages that contain images)

Design notes:
  - Page boundaries survive as <!-- page N --> markers so wiki pages can cite p.NN.
  - Two-column layouts (most journal papers) are detected per page by finding a
    vertical gutter, then each column is extracted separately so reading order
    is preserved instead of interleaved line-by-line.
  - Ruled tables are extracted to markdown; unruled ones survive as fixed-width
    text via the pdftotext -layout fallback. Both are marked "verify against PDF".
  - Output is a lossy working artifact. The PDF remains the source of truth.
"""
import re
import sys
import subprocess
import pathlib

GUTTER_MIN_FRAC = 0.025   # gutter must be >=2.5% of page width
GUTTER_SEARCH = (0.35, 0.65)   # look for it in the middle third
MIN_WORDS_FOR_COLUMN_TEST = 40


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80]


def find_gutter(words, width):
    """Return x of a vertical whitespace gutter near mid-page, or None."""
    if len(words) < MIN_WORDS_FOR_COLUMN_TEST:
        return None
    lo, hi = width * GUTTER_SEARCH[0], width * GUTTER_SEARCH[1]
    # occupancy histogram in 1pt bins across the search band
    bins = [0] * (int(hi - lo) + 1)
    for w in words:
        a, b = max(w["x0"], lo), min(w["x1"], hi)
        if b <= a:
            continue
        for i in range(int(a - lo), int(b - lo) + 1):
            if 0 <= i < len(bins):
                bins[i] += 1
    # longest run of empty bins
    best_len = best_start = run = start = 0
    for i, v in enumerate(bins):
        if v == 0:
            if run == 0:
                start = i
            run += 1
            if run > best_len:
                best_len, best_start = run, start
        else:
            run = 0
    if best_len >= width * GUTTER_MIN_FRAC:
        return lo + best_start + best_len / 2
    return None


def table_to_md(rows):
    rows = [[(c or "").replace("\n", " ").strip() for c in r] for r in rows]
    rows = [r for r in rows if any(r)]
    if len(rows) < 2:
        return None
    w = max(len(r) for r in rows)
    rows = [(r + [""] * w)[:w] for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * w]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    pdf, out = pathlib.Path(args[0]), pathlib.Path(args[1])
    (out / "figures").mkdir(parents=True, exist_ok=True)
    slug = slugify(pdf.stem)

    # pdftotext -layout as the per-page fallback / cross-check
    fallback = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        capture_output=True, text=True, check=True).stdout.split("\f")

    body = [
        "---",
        f"source_pdf: {pdf.name}",
        "converter: pdf2md.py (pdfplumber + pdftotext)",
        "note: lossy conversion — verify quantities and equations against the PDF",
        "---",
        "",
    ]
    n_two_col = n_tables = n_figpages = 0

    import pdfplumber
    with pdfplumber.open(str(pdf)) as doc:
        body.insert(2, f"pages: {len(doc.pages)}")
        for i, page in enumerate(doc.pages, 1):
            words = page.extract_words() or []
            gutter = None
            if "--single-col" not in flags:
                gutter = (page.width / 2 if "--two-col" in flags
                          else find_gutter(words, page.width))

            text = ""
            try:
                if gutter:
                    left = page.crop((0, 0, gutter, page.height)).extract_text() or ""
                    right = page.crop((gutter, 0, page.width, page.height)).extract_text() or ""
                    if left.strip() and right.strip():
                        text = left.rstrip() + "\n\n" + right.rstrip()
                        n_two_col += 1
                    else:
                        gutter = None
                if not gutter:
                    text = page.extract_text() or ""
            except Exception as e:
                print(f"[warn] p.{i}: {e}", file=sys.stderr)

            # fall back to pdftotext if pdfplumber came up short
            fb = fallback[i - 1] if i - 1 < len(fallback) else ""
            if len(text.strip()) < 0.6 * len(fb.strip()):
                text = fb

            if not text.strip() and not page.images:
                continue

            body.append(f"\n<!-- page {i} -->\n")
            body.append(text.rstrip())

            for t in (page.extract_tables() or []):
                md = table_to_md(t)
                if md:
                    n_tables += 1
                    body.append(f"\n**Table (p.{i}) — auto-extracted, verify against PDF:**\n\n{md}\n")

            if page.images:
                n_figpages += 1
                stem = out / "figures" / f"{slug}-tmp"
                subprocess.run(
                    ["pdftoppm", "-f", str(i), "-l", str(i), "-r", "150", "-png",
                     str(pdf), str(stem)], check=False, capture_output=True)
                for produced in sorted((out / "figures").glob(f"{slug}-tmp*.png")):
                    produced.rename(out / "figures" / f"{slug}-p{i:02d}.png")
                body.append(f"\n*[figure(s) on p.{i} → figures/{slug}-p{i:02d}.png]*\n")

    dest = out / f"{slug}.md"
    dest.write_text("\n".join(body))
    print(f"wrote {dest}\n  {n_two_col} two-column pages, {n_tables} tables, "
          f"{n_figpages} figure pages")


if __name__ == "__main__":
    main()
