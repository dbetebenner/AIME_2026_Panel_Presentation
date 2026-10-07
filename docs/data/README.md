# AIME-Con 2026 program coding

Data behind the opening chart of the moderator deck: how the 335 items in the printed program
relate to AI in assessment products, AI in measurement professionals' own work, and the
profession itself.

## Current coding (v2, 6 October 2026): three independent yes/no questions

**File:** `program-items-coded.csv`, one row per program item, with columns `product`,
`profession` and `norms` (each 1 or 0), a rationale, and the v1 code for comparison.

| Question | Items coded yes | Share of 335 |
|---|---|---|
| **product**: AI inside an assessment, learning or scoring product or service | 221 | 66% |
| **profession**: AI in how measurement professionals do their own work | 131 | 39% |
| **norms**: the profession itself (norms, roles, competencies, training, accountability, governance) | 22 | 7% |

Rows overlap: an item can be yes on more than one question. 48 items are both product and
profession; 15 of the 22 norms items are also profession items.

**How the coding was done**
- **Codebooks:** `methods/codebook-2d.md` and `methods/codebook-norms.md`, verbatim. These were the
  coders' only instructions.
- **Primary coder:** an AI coder (Claude) given only the codebook and the item text
  (`methods/items-text.jsonl`), blind to the v1 coding. Outputs: `methods/coder1-items.csv`,
  `methods/coder1-norms.csv`, `methods/coder1-sessions.csv`.
- **Second coder:** an independent AI coder (Claude, a separate instance) given only the codebook
  and a blind stratified sample of 98 items (`methods/second-coder-sample.json`, stratified on the
  v1 code and ambiguity, seed 20261006). Outputs: `methods/coder2-*.csv`.
- **Agreement** (`methods/agreement.json`, n = 98):

  | Question | Agreement | Cohen's κ |
  |---|---|---|
  | product | 91% | 0.80 |
  | profession | 97% | 0.94 |
  | norms | 94% | 0.72 |

  Both coders are the same model family, so agreement shows the codebook can be applied
  consistently. It is not independent human judgment.
- **Audit:** the chair reviewed the v1 profession list on 6 October with no changes.
  Disagreements and the items whose classification moved are listed in `methods/audit-2d.md` for
  the chair's audit. The primary coder's codes stand unless the chair changes them.
- **Reproduce:** `python3 data/methods/merge.py data/methods/coder2-norms.csv` rebuilds
  `program-items-coded.csv` and the norms agreement.

**Why v2:** an adversarial review (6 October) pointed out that v1's A/B categories were not
mutually exclusive: 81 of 335 items were flagged ambiguous, 48 of them A↔B. It also pointed out
that v1's tie rule pushed items toward "product". v2 drops the tie rule. The large shift is that
AI used as a psychometric method (difficulty prediction, calibration, item review, synthetic
respondents) now counts as professional work. Under v1 it counted as product. That is why v1's
9:1 became about 1.7:1. The **norms** question was added to separate *using AI in our work* from
*asking what AI means for the profession*.

---

## v1 coding (superseded; kept for comparison)

## Source

*2026 NCME Artificial Intelligence in Measurement and Education Conference* printed program
(`Assets/Damian_Betebenner-moderator/AIME-Con-2026-Program_sm-1.pdf`, 92 pp., created
2026-09-28). The text was extracted with `pdftotext -layout`, and only the FULL SCHEDULE pages
were parsed.

## Method

These files were coded by Claude (Opus 5.5) from the printed program on 2026-10-06, and
audited by the chair.

Each unit is judged from its title and its printed abstract or session description. Many
coordinated-session papers print a title only.

- **`program-sessions.csv`**: 83 sessions, one row per scheduled session.
  - Excluded: the break, the keynote overflow room, and two Sponsor Showcase slots with no
    title or content.
- **`program-presentations.csv`**: 335 presentations, one row per bulleted presentation.
  - Panels are one bullet each.
  - Training sessions, keynotes and the two titled sponsor sessions have no sub-presentations,
    so each counts as one session-level item. Their bulleted learning objectives are not
    presentations.
  - Includes the 24 posters, plus three presentations printed without a bullet (two in "AI for
    Mathematics: Scoring & Item Development", one in "Formative Assessment & Feedback").

`ambiguous = TRUE` marks rows where a reasonable coder could choose `alt_code`.

## Codebook (verbatim)

- **A = AI in assessment/education PRODUCTS & SERVICES:** automated scoring, AI item generation,
  AI tutors/chatbots, AI feedback, adaptive testing, item-parameter/difficulty prediction,
  AI-assisted test design/alignment, synthetic respondents used to build or evaluate assessment
  products, LLM judges for scoring, validity/fairness evidence FOR those AI products.
- **B = AI in the PROFESSIONAL WORK of measurement professionals themselves:** AI in their own
  workflows (coding, analysis, modeling assistance e.g. "LLMs to assist in IRT modeling",
  writing, documentation, simulation, research), peer review/publishing, professional
  roles/competencies/careers/hiring, graduate training & curricula for the profession,
  dissertations, norms/governance of professional practice.
- **C = neither:** no AI, or psychometric methods without AI, or general keynote/logistics where
  the content can't be judged, or AI literacy for students/teachers (not measurement
  professionals).

**Tie rule:** if an item builds or evaluates a tool that end-users (students, teachers,
test-takers) experience, code A. If it changes how the measurement professional does their job,
code B.

**Applied convention:** the enumerated A list takes precedence. AI used inside test-development
operations (item QA, DIF screening, enemy-item identification, item writing) is coded A and
flagged as ambiguous, with B as the alternative.

## v1 counts (the chair reviewed the B list on 6 October; no changes)

| Unit | n | A | B | C | B share of A+B |
|---|---:|---:|---:|---:|---:|
| Sessions | 83 | 70 (84.3%) | 10 (12.0%) | 3 (3.6%) | 12.5% |
| Presentations | 335 | 274 (81.8%) | 30 (9.0%) | 31 (9.3%) | 9.9% |

**Sensitivity.** "Firm B" counts only B rows that are not flagged as ambiguous. "B if every
ambiguous-to-B flips" also adds every row whose alternative code is B.

| Unit | Firm B | Coded B | B if every ambiguous-to-B flips |
|---|---:|---:|---:|
| Sessions | 6 (7.2%) | 10 (12.0%) | 19 (22.9%) |
| Presentations | 12 (3.6%) | 30 (9.0%) | 68 (20.3%) |
