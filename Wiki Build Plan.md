---
type: plan
created: 2026-08-25
updated: 2026-08-25
status: scaffolded — Phase 0 complete, ready for first ingest
---

# LLM Wiki — Build Plan

An instantiation of the [[LLM Wiki]] pattern for nuclear engineering research: HTGRs, TRISO fuel, graphite moderation, and Valar Atomics' design space. Primary inputs are research PDFs (IAEA/INL/ORNL/NRC reports, journal papers) converted to markdown.

## Decisions locked in

| Decision | Choice |
|---|---|
| Location | Inside this vault, under `Wiki/` — existing notes untouched |
| Existing notes | Excluded from the wiki; they stay as your personal layer |
| Conversion | Start with the built-in fallback converter; add `marker-pdf` only where it proves necessary |
| Ingest style | One source at a time, interactive |
| Figures | Extract selectively — the ones that carry information |
| Tone | Neutral reference prose; study material generated on demand |
| Long reports | Parent source page + per-chapter sub-pages (rare — most sources are 20–40pp papers) |
| Web sources | Second ingest path: Web Clipper markdown into `raw/web/`, no conversion |
| Valar framing | Confined to dedicated `valar/` pages; concept pages stay general |
| Scanned PDFs | Not expected — no OCR branch built |

## One constraint you should know about first

I can reach your vault files, but the shell I get is a **sandboxed Linux VM with no internet access** — not your Mac's terminal. That means:

- I **can** read, write, search, and edit anything under `Valar Atomics/`, and run `pdftotext`, `pdfplumber`, `pandoc`, `tesseract` against your PDFs today.
- I **cannot** install `marker-pdf` (or anything else from PyPI) for you, in that VM or in my cloud container.

This is why the fallback converter is the starting point: it runs entirely on my side, so ingesting a paper costs you nothing but dropping the PDF in a folder. Marker stays on the table as an upgrade you install and run on your Mac if and when the fallback demonstrably loses something you need.

---

## 1. Directory layout

```
Valar Atomics/                      ← vault root, your notes stay as-is
├── Nuclear Physics ... Mod 1.md    ← untouched
├── Valar's HTGR.md                 ← untouched
└── Wiki/
    ├── CLAUDE.md                   ← the schema. the most important file here
    ├── index.md                    ← catalog of every page (content-oriented)
    ├── log.md                      ← append-only timeline (chronological)
    ├── overview.md                 ← the evolving synthesis / thesis
    ├── sources/                    ← one page per ingested PDF
    │   └── <Long Report>/          ← sub-pages, for chaptered documents
    ├── concepts/                   ← physics + engineering concepts
    ├── entities/                   ← reactor designs, orgs, facilities, programs
    ├── data/                       ← cross-source parameter tables
    ├── questions/                  ← open questions + filed-back answers
    ├── valar/                      ← the only place Valar-specific framing lives
    ├── assets/                     ← figures referenced by wiki pages
    ├── bin/                        ← conversion + search scripts
    └── raw/                        ← immutable sources. LLM reads, never writes
        ├── pdf/                    ← originals, exactly as downloaded
        ├── md/                     ← converted markdown
        ├── web/                     ← clipped articles, already markdown
        └── figures/                ← page renders per source
```

`Wiki/raw` goes in Obsidian's **excluded files** list (Settings → Files and links). Converted markdown stays greppable on disk, but 200-page dumps don't pollute graph view or search.

**Why `data/` exists:** in this domain the recurring question is "what value does *this* source give for kernel diameter / enrichment / outlet temp / burnup limit / packing fraction," and sources disagree. A handful of cross-source comparison tables (TRISO particle specs, prismatic core parameters, materials properties, licensing milestones) is where the wiki earns its keep versus re-reading five PDFs.

---

## 2. Data format spec

### Naming

- Sources: `sources/AGR-2 Irradiation Test Final Report.md` — human-readable title, no dates or IDs in the filename (those go in frontmatter). Keeps `[[wikilinks]]` natural.
- Long-report sub-pages: `sources/AGR-2 Irradiation Test Final Report/Ch 4 — Fission Product Release.md`, each linked from the parent and each carrying its own page range.
- Concepts: singular noun phrases — `concepts/Resonance Escape Probability.md`, `concepts/Doppler Broadening.md`.
- Entities: the thing's actual name — `entities/TRISO.md`, `entities/MHTGR-350.md`, `entities/Valar Atomics.md`.
- Raw files keep the publisher's filename, slugified: `raw/pdf/inl-ext-21-64457-agr-2-final.pdf`.

### Frontmatter (all pages, so Dataview works later)

```yaml
---
type: source | source-chapter | concept | entity | data | question | synthesis
title: AGR-2 Irradiation Test Final Report
# source pages only:
authors: [Collin, B.P.]
org: INL
year: 2018
doc-id: INL/EXT-18-45xxx
url: https://...
pdf: raw/pdf/....pdf
md: raw/md/....md
pages: 312          # source-chapter pages: the range this covers, e.g. 88-134
ingested: 2026-08-25
# all pages:
status: stub | draft | solid
tags: [triso, fuel-performance, irradiation]
sources: 4          # non-source pages: how many sources feed this page
updated: 2026-08-25
---
```

### Source page template

```markdown
# <Title>
> <Org>, <year>. <doc-id>. [PDF](raw/pdf/...) · [converted](raw/md/...)

**Gist** — 3–5 sentences: what was done, what was measured, what it establishes.

## Key findings
- claim, with the number, with the page — `p.34`

## Data extracted
| Parameter | Value | Conditions | Page |

## Figures kept
![[assets/agr2-p34-fig12.png]] — one line on what it shows, `p.34`

## What this changes in the wiki
- confirms / refines / contradicts <existing claim on [[page]]>

## Open questions raised
- ...

## Chapters
- [[Ch 4 — Fission Product Release]] · pp.88–134   ← long reports only

## Pages updated on ingest
- [[TRISO]], [[Fuel Performance]], ...
```

### Concept page template

```markdown
# <Concept>
**In one line** — ...

## Mechanism
Reference prose. What it is, how it works, what governs it.

## Quantitative anchors
| Quantity | Value | Source | Page |

## Design implications for HTGRs
what this constrains in a prismatic, graphite-moderated, He-cooled core

## Contested / uncertain
> [!warning] Conflict
> [[Source A]] p.12 gives X; [[Source B]] p.88 gives Y. Unresolved because…

## Sources
- [[...]]
```

### Conventions the schema will enforce

- **Every number carries a source and a page.** No unsourced quantities on any page. This is the single rule that makes the wiki trustworthy at scale.
- **Page-accurate citations.** The converter writes `<!-- page N -->` markers into the raw markdown, so page numbers survive conversion and I can cite `p.34` rather than "somewhere in the report."
- **Reference tone.** Neutral, dense, built for lookup — not lecture notes. Ask and I'll generate study material, flashcards, or a Marp deck *from* the wiki; the wiki itself stays a reference layer.
- **Units: SI, explicit.** °C for temperature, MWth/MWe distinguished, %FIMA for burnup, barns for cross sections, µm for particle dimensions. Values converted from other units get the original in parentheses.
- **Conflicts are never silently resolved.** They get an Obsidian `> [!warning] Conflict` callout and a `#conflict` tag so a Dataview query can list every open disagreement in the wiki.
- **Confidence, when it's soft.** Vendor claims, pre-print results, and extrapolations get marked as such rather than stated flat.
- **Equations in `$…$` / `$$…$$`** — renders natively in Obsidian, survives round-tripping.
- **Links are wikilinks**, and a page mentioning a concept that has a page must link it. That bookkeeping is the LLM's job, not yours.
- **Valar framing lives only in `valar/`.** Concept pages discuss implications for HTGRs generally; `valar/Design Space.md` and `valar/Open Questions.md` read those concepts against what Valar is actually building and link out to them. Keeps concept pages reusable and stops the same paragraph being restated on forty pages.
- **Figures are kept when they carry information** — TRISO particle cross-sections, core and block layouts, flux and temperature profiles, irradiation performance plots, flowsheets. Skipped: org charts, project timelines, logos, decorative renders. Anything kept gets a caption line and a page citation; anything skipped is still recoverable from `raw/`.

### Long documents (the exception, not the rule)

Most sources will be 20–40 page journal papers that fit on one source page. When a 300-page TECDOC does turn up, it becomes a parent source page (gist, scope, chapter map, the cross-cutting findings) plus one sub-page per substantive chapter, each with its own page range in frontmatter. Ingested in passes rather than one sitting — you flag which chapters matter first, the rest can be filled in later or left as raw. Front matter, appendices of forms, and boilerplate don't get sub-pages.

---

## 3. Conversion pipeline

### Default — `bin/pdf2md.py` (built and tested, runs on my side)

`pdfplumber` for text and ruled tables with `pdftotext -layout` as a per-page fallback, `pdftoppm` to render figure-bearing pages at 150 dpi, plus `<!-- page N -->` markers throughout. **Two-column layouts are detected per page and each column extracted in reading order** — the thing that matters most now that journal papers are the dominant source type. Tested on both layouts. No install, no network, no step for you.

```bash
python3 Wiki/bin/pdf2md.py Wiki/raw/pdf/paper.pdf Wiki/raw/md/
```

What it handles well: born-digital papers and reports in one or two columns, ruled tables, figure-bearing pages flagged for review. What it loses: inline equations in dense layouts (garbled), and unruled tables (kept as fixed-width text — readable, not machine-readable). `--two-col` / `--single-col` force the behaviour when detection guesses wrong.

**The mitigation matters more than the converter.** On every ingest I also read the original PDF pages directly — for figures, for equations that look mangled, and to spot-check anything the conversion may have dropped. LLM PDF reading and text extraction fail in different places, and the cross-check is cheap. Converted markdown is a lossy working artifact, never the source of truth.

### Upgrade path — `marker-pdf` on your Mac

If we find the fallback is systematically costing us on your actual sources — dense equation derivations, two-column journal papers, tables you need machine-readable — then:

```bash
uv tool install marker-pdf                    # ~2 GB, one time
export TORCH_DEVICE=mps                       # Apple Silicon GPU
marker_single "paper.pdf" --output_dir "…/Wiki/raw/md" --output_format markdown
```

Equations → LaTeX, tables → markdown tables, figures extracted as files, reading order preserved. Cost is the install plus a command you run per paper. We'll decide this from evidence after the first few ingests, not up front.

### Web clips

Obsidian Web Clipper output goes straight into `raw/web/` — already markdown, no conversion. Same ingest loop otherwise. Two differences the schema encodes: web sources have no page numbers, so they're cited by section heading; and they're weaker evidence than peer-reviewed or lab-published work, which the wiki says out loud when they conflict.

*(No OCR branch built — you don't expect scanned sources. `tesseract` is available on both sides if that changes; it's about ten minutes of work.)*

---

## 4. Operations

### Ingest (interactive, one source at a time)

1. You drop the PDF in `Wiki/raw/pdf/` and tell me it's there.
2. I convert it, read the markdown end to end, and open the original pages for figures and anything that converted badly.
3. **We talk first, before anything is written.** I bring you 5–10 takeaways, flag what's genuinely new versus what the wiki already has, and name any contradictions with existing pages. You steer what matters and what to skip. For long reports, this is also where you pick which chapters get sub-pages.
4. I then write, in one pass: the source page, new/updated concept and entity pages, any `data/` table rows this source touches, kept figures into `assets/`, cross-links in both directions, an `index.md` entry, and a `log.md` line.
5. I report the changelog — every file created or modified, one line each — and you browse it in Obsidian.

Web clips follow the same loop minus step 2's conversion.

Expect a substantive paper to touch 5–12 pages. Expect the first three ingests to change the schema; that's the point of doing them slowly.

### Query

Ask a question; I read `index.md`, drill into the relevant pages, answer with citations back to source pages and PDF page numbers. When the answer is worth keeping — a comparison, a derivation, a synthesis across sources — it gets filed into `questions/` or `data/` as a real page rather than evaporating into chat. Output can also be a Marp deck or a matplotlib chart when that's the better form.

### Lint (roughly every 5–10 sources)

I sweep for: contradictions between pages, claims superseded by newer sources, orphan pages, concepts referenced repeatedly but lacking a page, missing back-links, `status: stub` pages that never grew, and gaps where a targeted search for a specific paper would pay off. Output is a punch list you approve or reject, plus suggested next sources to hunt down.

### index.md and log.md

`index.md` — grouped by category, one line per page: link, one-sentence summary, source count, status. I rewrite the affected section on every ingest.

`log.md` — append-only, fixed prefix so it's greppable:

```
## [2026-08-25] ingest | AGR-2 Irradiation Test Final Report
touched: TRISO, Fuel Performance, Burnup Limits, index
notes: burnup limit conflicts with [[MHTGR-350 PSID]] — flagged
```

`grep "^## \[" log.md | tail -5` gives you the recent history in one line.

---

## 5. Phases

**Phase 0 — scaffold. ✅ Done.** Directory tree, `CLAUDE.md`, `index.md` / `log.md` / `overview.md`, the two `valar/` pages, `bin/pdf2md.py`, `.gitignore`, `git init`. Two things left for you: add `Wiki/raw` to Obsidian's excluded files (Settings → Files and links), and make the first git commit from your Mac (`git add -A && git commit -m "scaffold"` inside `Wiki/` — I can't commit from my sandbox, it isn't allowed to delete git's temp files).

**Phase 1 — first ingest.** You drop in one real paper — ideally one you already know something about, so you can judge the output. We run the full ingest loop end to end and see what the conversion and the templates actually produce on real material.

**Phase 2 — ingests two and three.** Deliberately slow. After each we revise `CLAUDE.md`: page templates that didn't fit, a category that's missing, a citation convention that's annoying in practice. Also the point where we decide whether marker is worth installing. The schema is the deliverable of this phase as much as the pages are.

**Phase 3 — build out (ongoing).** Ingest at whatever rate you're reading. First lint pass at ~5 sources. Add Dataview dashboards once frontmatter has proven stable — "all pages with open conflicts," "sources by year," "stub pages," "concepts with fewer than 2 sources."

**Phase 4 — scale, only if needed (~50+ sources).** If `index.md` stops being enough for retrieval, add proper search: `qmd` (hybrid BM25 + vector, local, has an MCP server) on your Mac, or a plain `ripgrep` wrapper in `bin/`. Don't build this before it hurts.

---

## 6. Failure modes to design against

- **Summary drift** — concept pages slowly become the LLM's paraphrase of a paraphrase. Mitigated by the every-number-carries-a-page rule: anything traceable can be re-verified against the raw markdown, and the raw markdown against the PDF.
- **Over-fragmentation** — 400 concept pages with two sentences each. Mitigated by a rule in the schema: a concept gets its own page only when it has content from 2+ sources or is genuinely load-bearing; otherwise it lives as a section on a parent page until it earns promotion.
- **Silent conversion loss** — a table or key equation the converter dropped, which then never enters the wiki. Mitigated by the direct-PDF cross-check on ingest, and by keeping originals immutable.
- **Schema rot** — `CLAUDE.md` describes a workflow neither of us follows anymore. Mitigated by revisiting it at each lint pass.

---

## 7. Resolved

All four open questions answered 2026-08-25: mostly 20–40 page papers (so chapter-splitting is the exception); Valar framing confined to dedicated pages; no scanned sources; web clips get their own ingest path. Nothing outstanding — the next decision point is whether `marker-pdf` is worth installing, and we take that from evidence after the first few ingests.
