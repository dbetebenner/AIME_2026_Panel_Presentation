# Educational Measurement as an AI-Native Profession

Materials for the AIME-Con 2026 panel *Educational Measurement as an AI-Native Profession*:
**Wednesday 7 October 2026, 11:00 AM–12:30 PM, Commonwealth 2, Wyndham Grand Pittsburgh Downtown.**

**Public site:** <https://dbetebenner.github.io/AIME_2026_Panel_Presentation/>

| Role | |
|---|---|
| Session chair | Damian Betebenner, Center for Assessment |
| Moderator | lain, an AI interlocutor operating under the session chair's supervision |
| Panelists | Damian Betebenner · Derek Briggs (University of Colorado Boulder) · Frank Rijmen (Cambium Assessment) · Mohammed A. A. Abulela (MetaMetrics, Inc. / University of Minnesota, with Guher Gorgun, Brian French, Brian Leventhal and Matthew Gushta) |
| Discussant | Fred Oswald, University of California, Irvine |

## What this repository is for

The repository does three jobs:

1. **Shares the panel's materials with the audience.** Each presenter's files are published as
   they supplied them, on a GitHub Pages site the audience reaches by a QR code on the framing slides.
2. **Holds the slides presented in the room.** These are the moderator's framing deck and the
   provocation decks, as self-contained HTML that works offline, with PDF backups.
3. **Is the source of the AI moderator's corpus.** lain draws only on the panelists' materials (no
   open web). The text versions in `corpus/` are what it was given, so its citations can be
   checked against them.

All materials are shared publicly with the presenters' permission.

## Layout

| Path | Contents |
|---|---|
| `Assets/` | **The presenters' originals, unchanged:** slides (`.pptx`), papers and briefs (`.docx`), statements and bios (`.md`), and the final session proposal (`.tex`). One folder per presenter. |
| `decks/` | Quarto revealjs sources: `moderator.qmd` (the 0–6 min framing), `betebenner-provocation.qmd`, and `briggs-provocation.qmd` (built from Derek Briggs's statement, verbatim). |
| `rendered/` | PDF copies: the decks, the PowerPoint files exported with Keynote, and the compiled proposal. Each is labeled on the site as a rendered copy; the originals are authoritative. |
| `corpus/` | Text versions of files that are hard to read or index: `.docx` converted to markdown, slide text with speaker notes, and Mohammed Abulela's slide text transcribed from the slide images. |
| `data/` | The opening chart's data: every item in the AIME-Con 2026 printed program, coded as AI built into assessment products (A), AI in how measurement professionals work (B), or neither (C). Coded by an AI and audited by the chair; the codebook and method are in `data/README.md`. |
| `index.qmd`, `_quarto.yml` | The site: one card per contributor with originals, rendered copies and provocation statements. |
| `theme/` | Styles built from the dataimago design tokens (Noto Sans; the house presentation theme). |
| `figures/` | Generated QR codes for the audience view and this site. |
| `docs/` | The rendered site that GitHub Pages serves. Generated: do not edit by hand. |

The conference program PDF the chart was coded from is kept locally (`Assets/Damian_Betebenner-moderator/`,
gitignored) and is not republished here. See the official AIME-Con 2026 site.

## Building

Requirements: [Quarto](https://quarto.org) 1.8+, R with `ggplot2`, `dplyr`, `readr` and `qrcode` (for the chart and QR codes in the moderator deck), and Noto Sans installed.

```sh
quarto render                 # site + decks → docs/
```

Deck PDFs are printed from the rendered HTML with [decktape](https://github.com/astefanutti/decktape) while `docs/` is served locally:

```sh
(cd docs && python3 -m http.server 8765) &
npx decktape reveal --size 1600x900 http://localhost:8765/decks/moderator.html rendered/moderator-slides.pdf
```

Push to `main` and GitHub Pages republishes from `main:/docs`.

## Conventions

- **Originals are never edited.** A presenter's update replaces their file in `Assets/`, and the
  rendered copy and text version are regenerated from it.
- The AI interlocutor's name is **lain**, always lower case.
