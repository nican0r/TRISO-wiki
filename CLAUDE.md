# Wiki schema

You are the maintainer of this wiki. This file tells you how it is structured and how to work in it. Read it at the start of every session, and revise it when a convention here stops matching what we actually do.

## Domain

Nuclear engineering research: high-temperature gas reactors, TRISO fuel, graphite moderation and reflection, HALEU, fuel performance and qualification, and the design space Valar Atomics is working in. Sources are research papers and technical reports, mostly 20–40 page journal papers, some longer IAEA/INL/ORNL/NRC reports.

## Layers and ownership

- `raw/` — immutable. Read from it, never write to it except by running the converter. Original PDFs in `raw/pdf/`, converted markdown in `raw/md/`, clipped web articles in `raw/web/`, page renders in `raw/figures/`.
- Everything else under `Wiki/` — yours. You create, update, cross-link, and reorganize these pages.
- **Everything outside `Wiki/` is off-limits.** The vault root holds Nelson's own study notes (`Nuclear Physics and Reactor Theory ...`, `Valar's HTGR.md`, `HTGR Overview ...`, `Todo.md`, and so on). Do not read them as sources, do not edit them, do not link to them. They are a separate personal layer by explicit decision.

## Layout

```
Wiki/
├── CLAUDE.md      this file
├── index.md       catalog of every page (content-oriented)
├── log.md         append-only timeline (chronological)
├── overview.md    the evolving synthesis
├── sources/       one page per ingested source
├── concepts/      physics and engineering concepts
├── entities/      reactor designs, orgs, facilities, programs, materials
├── data/          cross-source parameter tables
├── questions/     open questions and filed-back answers
├── valar/         the only place Valar-specific framing lives
├── assets/        figures kept from sources
├── bin/           pdf2md.py and any future tooling
└── raw/           immutable sources
```

## Frontmatter

Every page carries YAML frontmatter. Dataview queries depend on it staying consistent.

```yaml
---
type: source | concept | entity | data | question | synthesis | valar
title: AGR-2 Irradiation Test Final Report
# sources only:
authors: [Collin, B.P.]
org: INL
year: 2018
doc-id: INL/EXT-18-45xxx
url: https://...
pdf: raw/pdf/....pdf
md: raw/md/....md
ingested: 2026-08-25
# everything:
status: stub | draft | solid
tags: [triso, fuel-performance, irradiation]
sources: 4        # non-source pages: how many sources feed this page
updated: 2026-08-25
---
```

## Naming

- Sources: the document's human title — `sources/AGR-2 Irradiation Test Final Report.md`. Dates and IDs live in frontmatter, not filenames.
- Concepts: singular noun phrases — `concepts/Resonance Escape Probability.md`.
- Entities: the thing's actual name — `entities/TRISO.md`, `entities/MHTGR-350.md`.
- Long reports only: a folder `sources/<Title>/` of chapter sub-pages, each with a `pages:` range. Rare — most sources are short enough for one page.

## Hard rules

1. **Every number carries a source and a page.** No unsourced quantity appears anywhere in this wiki. Format: `950 °C ([[Source Title]] p.34)`. If a number cannot be traced, it does not go in.
2. **Cite page numbers from the `<!-- page N -->` markers** the converter writes into `raw/md/`. Verify against the PDF when a number matters.
3. **Reference tone.** Neutral, dense, written for lookup — not lecture notes, not bullet-fragment study material. Study material, flashcards, and Marp decks are generated on request *from* the wiki; they are not what the wiki is. Dense means brief — see rule 12.
4. **Units: SI, explicit.** °C, MWth vs MWe distinguished, %FIMA for burnup, barns for cross sections, µm for particle dimensions. Converted values keep the original in parentheses.
5. **Never silently resolve a conflict.** When sources disagree, both claims stay, in a callout, on the relevant page:
   ```
   > [!warning] Conflict
   > [[Source A]] p.12 gives 19.6 %FIMA; [[Source B]] p.88 gives 16.4 %FIMA. Different test conditions — unresolved.
   ```
   Tag the page `#conflict` so a Dataview query can list every open disagreement.
6. **Mark soft claims.** Vendor figures, pre-prints, extrapolations, and single-source claims are labelled as such rather than stated flat.
6a. **Mark wiki inferences.** A conclusion derived here rather than stated in a source — reconciling two figures, deriving a value, inferring a mechanism — goes in a `> [!info]` callout tagged `#inferred`, naming what it was derived from and what would confirm it. Never let an inference read as a source statement. A resolved inference stops carrying `#conflict`; `#conflict` means an open disagreement, `#inferred` means a filled gap.
7. **Equations in `$…$` and `$$…$$`.** Renders natively in Obsidian.
8. **Link everything linkable.** A page that mentions a concept with its own page must `[[link]]` it, and the target page's Sources or Related section links back. This bookkeeping is your job.
9. **Promotion rule.** A concept gets its own page when it draws on 2+ sources or is genuinely load-bearing. Below that it lives as a section on a parent page. Prefer few substantial pages over many thin ones.
10. **Skip history that does not explain function.** Programme chronologies, which country built what and when, and design decisions justified by a specific historical reactor are out of scope. Historical material stays only where it explains how fuel or an HTGR *works* or establishes a present-day standard — German coating parameters and matrix chemistry are kept, because they define the reference process; the operating history of the AVR or THTR is not, unless a specific result is the evidence for a mechanism. When a historical fact is the only evidence for a technical claim, keep the claim and cite the evidence in one clause, not the narrative.
11. **Define acronyms on first use.** Any acronym that is not universally standard gets expanded the first time it appears on a page — `%FIMA` (fissions per initial metal atom), `IPyC` (inner pyrocarbon), `KÜFA` (Cold Finger Apparatus) — or is wikilinked to a page that defines it. First use is *per page*, not per wiki: a reader arriving at a concept page from a search should not have to open another page to parse the first paragraph. Expand once, then use the acronym freely for the rest of the page.
    Chemical formulae and unit symbols are exempt (UO₂, SiC, MPa, °C). Domain terms a nuclear engineer would not pause on are exempt (LWR, HTGR, TRISO). When in doubt, expand — it costs four words.
    **Watch for collisions.** In this source alone, `AGR` means both the British Advanced Gas Reactor line ([[Ch 01 — Introduction]] p.12) and the US Advanced Gas Reactor fuel development programme ([[Ch 05 — Fabrication of Fuel Compacts]] p.51). Where an acronym is ambiguous, disambiguate rather than expand — "the US AGR fuel programme" — and say so once on the page.
12. **Brevity is the default; length must be earned.** Write the minimum that carries the claim and its citation. Concretely:
    - **Do not restate what another page already establishes.** Link it. A concept page that re-explains the TRISO layer stack instead of linking [[TRISO Particle Architecture]] is duplicating maintenance, and the two copies will drift.
    - **Prefer a table to prose** for anything with more than two parallel values. Prefer one sentence with a number and a page over three sentences of context around it.
    - **Cut the connective tissue.** No restating the section heading in the first line, no "it is worth noting that", no closing summary of what was just said.
    - **One idea per section.** If a section has grown past roughly 150 words, either it contains two ideas that want splitting, or it contains restatement that wants deleting.
    - **A gist is 3–5 sentences and stays that way.** Findings go under headings, not in the gist.
    Density and brevity are the same requirement, not opposites: a dense page says more per word, which means fewer words for the same content. Cut until removing the next word would remove a fact or a citation.
13. **Valar framing is confined to `valar/`.** Concept pages discuss implications for HTGRs generally; the Valar-specific reading lives in `valar/` pages that link out to the concepts. Do not add "relevance to Valar" sections to concept pages.

## Page templates

### Source

```markdown
# <Title>
> <Org>, <year>. <doc-id>. [PDF](raw/pdf/...) · [converted](raw/md/...)

**Gist** — 3–5 sentences: what was done, what was measured, what it establishes.

## Key findings
- claim with the number — `p.34`

## Data extracted
| Parameter | Value | Conditions | Page |

## Figures kept
![[assets/<slug>-p34-fig12.png]] — what it shows, `p.34`

## What this changes in the wiki
- confirms / refines / contradicts <claim on [[page]]>

## Open questions raised
- ...

## Pages updated on ingest
- [[...]]
```

### Concept

```markdown
# <Concept>
**In one line** — ...

## Mechanism
Reference prose: what it is, how it works, what governs it.

## Quantitative anchors
| Quantity | Value | Source | Page |

## Design implications for HTGRs
What this constrains in a prismatic, graphite-moderated, helium-cooled core.

## Contested / uncertain
> [!warning] Conflict
> ...

## Sources
- [[...]]
```

### Entity, data, question, valar

Same frontmatter and citation rules; structure to fit. `data/` pages are a table plus a note on how the sources' conditions differ — that context is what makes the comparison honest. `questions/` pages state the question, what the wiki can currently answer, and what is missing.

## Conversion

```bash
python3 Wiki/bin/pdf2md.py Wiki/raw/pdf/<file>.pdf Wiki/raw/md/
```

Detects two-column layouts per page and extracts each column in reading order; extracts ruled tables to markdown; renders figure-bearing pages to `raw/md/figures/<slug>-pNN.png`; writes `<!-- page N -->` markers throughout. Flags `--two-col` / `--single-col` force the behaviour when detection gets it wrong.

It is lossy. Inline equations in dense layouts and unruled tables degrade. **On every ingest, also read the original PDF pages directly** for figures, equations, and anything that looks garbled — text extraction and direct PDF reading fail in different places, and the cross-check is cheap. When the two disagree, the PDF wins.

Web clips (Obsidian Web Clipper markdown) go straight into `raw/web/` — no conversion step. They carry no page numbers, so cite them by section heading instead.

## Workflows

### Ingest — PDF

1. Convert the PDF into `raw/md/`.
2. Read the converted markdown end to end. Open the original PDF pages for figures and anything that converted badly.
3. **Discuss before writing.** Bring 5–10 takeaways, say plainly what is new versus what the wiki already has, and name every contradiction with an existing page. Let Nelson steer emphasis. Write nothing until this exchange has happened.
4. Then, in one pass: the source page; new and updated concept and entity pages; any `data/` rows this source touches; kept figures copied into `assets/`; cross-links in both directions; an `index.md` entry; a `log.md` line.
5. Report the changelog — every file created or modified, one line each.

Keep figures that carry information: TRISO cross-sections, core and block layouts, flux and temperature profiles, irradiation performance plots, flowsheets. Skip org charts, timelines, logos, decorative renders.

### Ingest — web clip

Same loop, minus conversion. Source page frontmatter uses `url:` and omits `pdf:`/`md:`. Web sources are weaker evidence than peer-reviewed or lab-published work, and the page should say so when they conflict.

### Query

Read `index.md` first, then drill into the pages it points to. Answer with citations back to source pages and PDF page numbers. When the answer is worth keeping — a comparison, a derivation, a synthesis — file it into `questions/` or `data/` as a real page rather than leaving it in chat. Offer a Marp deck or a matplotlib chart when that form fits better.

### Lint — every 5–10 sources

Sweep for: contradictions between pages, claims superseded by newer sources, orphan pages, concepts referenced repeatedly with no page of their own, missing back-links, `status: stub` pages that never grew, `data/` tables with holes a specific paper would fill, **unexpanded acronyms on first use (rule 11)**, **sections past ~150 words and passages restating what another page already says (rule 12)**. Output a punch list for approval, plus suggested next sources to look for. Do not act on it unilaterally.

## index.md and log.md

`index.md` — grouped by category, one line per page: link, one-sentence summary, source count, status. Rewrite the affected section on every ingest.

`log.md` — append-only, fixed prefix so `grep "^## \[" log.md | tail -5` works:

```
## [2026-08-25] ingest | AGR-2 Irradiation Test Final Report
touched: TRISO, Fuel Performance, Burnup Limits, index
notes: burnup limit conflicts with [[MHTGR-350 PSID]] — flagged
```

Log queries and lint passes the same way, with `query |` and `lint |` prefixes.
