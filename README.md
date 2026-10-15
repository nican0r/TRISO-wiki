# TRISO / HTGR research wiki

A reference wiki on high-temperature gas-cooled reactors and TRISO coated particle fuel, built page by page from primary literature: journal papers, IAEA documents, and INL/ORNL technical reports. It is written for lookup, not for reading end to end.

Start at [`index.md`](index.md) for the catalog, [`overview.md`](overview.md) for the synthesis, and [`log.md`](log.md) for what changed when.

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

### Asking an LLM questions against the wiki

The point of the citation rules is that an assistant reading this vault can be held to them. Three ways to wire one up, in increasing order of control:

- **Inside Obsidian** — install the [Copilot](https://github.com/logancyang/obsidian-copilot) community plugin, add an API key for your provider (OpenRouter, Anthropic, OpenAI, Gemini, or any OpenAI-compatible or local model), let it index the vault, and use **Vault QA** mode, which answers from retrieved notes rather than from the model's own knowledge. After adding pages, re-run **Force Re-Index** from the command palette, and check **List Indexed Files** if an answer looks like it missed something.
- **An external chat client** — the [MCP Vault Bridge](https://community.obsidian.md/plugins/mcp-vault-bridge) plugin exposes the vault read-only over MCP on `127.0.0.1` behind a bearer token, so Claude Desktop, LM Studio or any MCP client can search and read these pages directly. Note that a cloud model sees whatever it retrieves.
- **An agent in the folder** — point Claude Code, Cowork or a similar coding agent at the clone. It reads `CLAUDE.md` on its own, which is how the wiki is maintained, and it can follow `[[wikilinks]]` and open `raw/md/` to check a citation against the converted source.

Because every claim here carries its source and page, you can check an answer by opening the page it cites — and the converted text in `raw/md/` carries `<!-- page N -->` markers, so you can go one step further to the original wording.

## Adding a source

**1. Put the document in `raw/`.** PDFs go in `raw/pdf/`, web clips (Obsidian Web Clipper markdown) go straight into `raw/web/`. Use a short descriptive filename — `review-of-sic-coating-properties.pdf`, not `1-s2.0-S014919702500160X-main.pdf`. Nothing else in `raw/` is ever edited by hand.

Download the actual PDF, not the publisher's article page: a saved ScienceDirect or Springer page usually contains only the abstract, and the ingest will stall on it.

**2. Convert it.** The converter needs Python 3 with `pdfplumber`, plus `pdftotext` and `pdftoppm` from Poppler (`brew install poppler` / `apt install poppler-utils`):

```bash
python3 bin/pdf2md.py raw/pdf/<file>.pdf raw/md/
```

It detects two-column layouts per page (`--two-col` / `--single-col` force it when detection is wrong), extracts ruled tables, renders figure-bearing pages, and writes `<!-- page N -->` markers that citations refer to. It is lossy: equations and unruled tables degrade, so read the original PDF alongside the conversion and let the PDF win where they disagree. An agent working in the folder will normally run this step for you.

**3. Ask the assistant to ingest it.** With an agent pointed at the clone (see above), the request is simply:

> Ingest `raw/pdf/<file>.pdf` into the wiki, following the ingest workflow in CLAUDE.md.

What should happen next, in order: it converts and reads the source end to end, opens the original PDF for figures and anything that converted badly, and then **comes back to you with 5–10 takeaways, what is new versus what the wiki already says, and every contradiction with an existing page — before writing anything.** That exchange is where you steer emphasis and decide whether a finding deserves its own page. If the assistant starts writing pages without it, stop it and ask for the takeaways first.

Only then does it write, in one pass: the source page, new and updated concept and entity pages, any `data/` rows the source touches, figures copied into `assets/`, cross-links in both directions, an `index.md` entry and a `log.md` line — finishing with a changelog of every file it touched. Commit one source per commit.

Citations use the PDF page markers from `raw/md/`, which can differ from the printed page numbers; where they do, each source page states the offset in its header.
