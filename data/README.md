# AIME-Con 2026 program coding

Data behind the opening chart of the moderator deck: how the program's sessions and
presentations divide between AI *in assessment products* and AI *in the professional work of
measurement*.

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

## Counts (pre-audit)

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
