# Codebook: two dimensions (v2, 6 Oct 2026)

Each program item (or session) is coded on **two independent yes/no questions**. Both can be yes.
Code what the item is *about*, from its title and abstract only. Do not infer effects the text
does not address. If the text is too thin to decide, code from the title and mark confidence `low`.

## product: Does the item concern AI inside an assessment, learning, or scoring product or service?

**Yes** when its subject is an AI capability that produces scores, items, feedback, tutoring or
other content that test-takers, students or teachers encounter, or evidence about such a capability.
Includes automated scoring, AI item or passage generation, AI tutors and chatbots for learners, AI
feedback, adaptive testing driven by AI, AI-generated learning content, synthetic respondents used
to build or validate such products, and validity, fairness or reliability evidence *for* such products.

**No** otherwise.

## profession: Does the item concern how measurement professionals do their own work with AI?

**Yes** when its subject is AI changing the work of psychometricians, assessment developers,
measurement researchers or testing-program staff. Includes AI in their analysis, coding,
modeling, simulation, writing and documentation; AI assisting item writers or item reviewers;
AI in peer review, standard setting, operational quality control, test assembly or test
security review; AI coding of research data (qualitative coding, survey responses); and
professional roles, competencies, careers, training, curricula and norms of practice.

**No** otherwise.

## Notes

- An AI tool that helps item writers produce items that reach students is **both** if the
  item addresses both the writers' work and the product; code what the text actually addresses.
- AI literacy for students or teachers is not about measurement professionals: profession = no.
- No AI focus at all: both no.

## Output, one line per item

`id,product,profession,confidence,rationale`, with product and profession as 1 or 0,
confidence `high` or `low`, and a rationale of at most 20 words.
