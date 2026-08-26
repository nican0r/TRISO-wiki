#!/usr/bin/env python3
"""Split a marker --paginate_output markdown file into per-chapter files.

Usage: split_chapters.py <marker_output.md> <out_dir>

Detects numbered chapter headings plus ANNEX / REFERENCES / ABBREVIATIONS,
converts marker's {N}----- separators into <!-- page N --> markers (1-based,
matching the PDF's physical pages), rewrites sibling image links, and writes
one file per chapter with frontmatter carrying its page range.
"""
import re, sys, pathlib

CH = re.compile(r"^#{1,6}\s+\**\s*(\d{1,2})\.\s+([A-Z][A-Z \-/&,\.]{5,}?)\**\s*$", re.M)
TAIL = re.compile(r"^#{1,6}\s+\**(ANNEX|REFERENCES|ABBREVIATIONS|CONTRIBUTORS)", re.M)


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def main(src, outdir):
    src = pathlib.Path(src)
    out = pathlib.Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    t = src.read_text()

    seps = [(m.start(), int(m.group(1)) + 1) for m in re.finditer(r"^\{(\d+)\}-{5,}", t, re.M)]
    if not seps:
        sys.exit("no {N}----- separators found — was marker run with --paginate_output?")

    def page_at(pos):
        p = 1
        for s, n in seps:
            if s <= pos:
                p = n
            else:
                break
        return p

    marks = []
    seen = set()
    for m in CH.finditer(t):
        n = int(m.group(1))
        if n in seen or page_at(m.start()) < 10:
            continue          # skip the table of contents
        seen.add(n)
        marks.append((m.start(), f"{n:02d}", m.group(2).strip().rstrip("*").strip().title()))
    for m in TAIL.finditer(t):
        if page_at(m.start()) < 10:
            continue
        name = m.group(1).title()
        if any(x[2] == name for x in marks):
            continue
        marks.append((m.start(), {"Annex": "15", "References": "16",
                                  "Abbreviations": "17", "Contributors": "18"}[name], name))
    marks.sort()
    marks.insert(0, (0, "00", "Front Matter"))

    written = []
    for i, (start, num, title) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(t)
        body = t[start:end]
        p0, p1 = page_at(start), page_at(end - 1)
        body = re.sub(r"^\{(\d+)\}-{5,}",
                      lambda m: f"<!-- page {int(m.group(1)) + 1} -->", body, flags=re.M)
        body = body.replace("](_page_", "](../_page_")
        fm = (f"---\ntype: source-chapter\nchapter: {num}\ntitle: {title}\n"
              f"pages: {p0}-{p1}\nsource_md: {src.name}\n---\n\n")
        dest = out / f"ch{num}-{slugify(title)}.md"
        dest.write_text(fm + body.lstrip())
        written.append((dest.name, p0, p1, len(body)))

    for name, p0, p1, n in written:
        print(f"{name:52s} pp.{p0}-{p1:<4d} {n//1024:4d} KB")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
