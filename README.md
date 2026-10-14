# TRISO / HTGR research wiki

A reference wiki on high-temperature gas-cooled reactors and TRISO coated particle fuel, built page by page from primary literature: journal papers, IAEA documents, and INL/ORNL technical reports. It is written for lookup, not for reading end to end.

Current contents: 10 ingested documents (one of them a 9-chapter handbook), 19 concept pages, 2 cross-source data tables, 2 answered questions, 59 figures, ~64,000 words. Start at [`index.md`](index.md) for the catalog, [`overview.md`](overview.md) for the synthesis, and [`log.md`](log.md) for what changed when.

## The rules that make it useful

Full schema in [`CLAUDE.md`](CLAUDE.md). The four that matter most to a reader:

1. **Every number carries a source and a page** — `950 °C ([[Source Title]] p.34)`. Nothing unsourced goes in.
2. **Disagreements are preserved, not resolved.** Where two sources conflict, both claims stay in a `> [!warning] Conflict` callout tagged `#conflict`.
3. **Conclusions drawn here are marked.** Anything derived rather than stated by a source sits in a `> [!info]` callout tagged `#inferred`, naming what it came from and what would confirm it.
4. **Vendor figures, pre-prints, single-source claims and extrapolations are labelled as such** rather than stated flat.

So `#conflict` lists the open disagreements and `#inferred` lists the gaps the wiki filled itself — both are searchable.

## Layout

```
index.md      catalog of every page
overview.md   the evolving synthesis
log.md        append-only timeline, one entry per ingest, query or lint
CLAUDE.md     the schema: rules, page templates, workflows
sources/      one page per ingested document
concepts/     physics and engineering concepts
data/         cross-source parameter tables
questions/    open questions and filed-back answers
valar/        design-specific framing, kept out of the concept pages
assets/       figures kept from sources
bin/          pdf2md.py, the ingest converter
raw/          immutable originals: pdf/, md/, web/
```

## Using it locally

```bash
git clone https://github.com/nican0r/TRISO-wiki.git
```

It is plain Markdown — readable in any editor. For the links and figures to work, open the folder as an [Obsidian](https://obsidian.md) vault (or drop it inside an existing one): pages cross-reference with `[[wikilinks]]`, figures embed with `![[assets/...]]`, and equations use `$…$` / `$$…$$`. The YAML frontmatter on every page (`type`, `status`, `tags`, `sources`, `updated`) is there so Dataview queries work if you install that plugin.

**The source PDFs are not in the repo.** `raw/pdf/` is gitignored — the originals are large and mostly copyrighted. Every page in `sources/` carries the document's title, report number or DOI, and a URL, so you can fetch the original yourself; most are free government reports. `raw/md/` holds the converted text, which is what page citations refer to.

## Adding a source

The converter needs Python 3 with `pdfplumber`, plus `pdftotext` and `pdftoppm` from Poppler (`brew install poppler` / `apt install poppler-utils`):

```bash
python3 bin/pdf2md.py raw/pdf/<file>.pdf raw/md/
```

It detects two-column layouts per page (`--two-col` / `--single-col` force it), extracts ruled tables, renders figure-bearing pages, and writes `<!-- page N -->` markers used for citations. It is lossy: equations and unruled tables degrade, so **read the original PDF alongside the conversion** and let the PDF win where they disagree.

Then follow the ingest workflow in `CLAUDE.md`: read the source end to end, bring the takeaways and every contradiction with an existing page before writing, then write the source page, update the concept and data pages it touches, cross-link both directions, add an `index.md` entry and a `log.md` line, and report the changelog. Commits are one per ingested source.

Citations use the PDF page markers from `raw/md/`, which can differ from the printed page numbers; where they do, each source page states the offset in its header.
