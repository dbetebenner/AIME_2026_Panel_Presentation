# Codebook addendum: the norms dimension (v2.1, 6 Oct 2026)

A third, independent yes/no question, coded from the item's title and abstract only.

## norms: Does the item address the measurement profession itself?

**Yes** when a subject of the item is the profession: its norms or standards of practice, its
roles, competencies, careers or hiring, its training or curricula, its accountability,
disclosure, verification or review responsibilities, or the governance of how measurement
professionals use AI. An item can be yes while also presenting a technical method, as long as
the professional question is part of what the item is about.

**No** when the item uses AI as a technical method or tool (for example to predict item
difficulty, calibrate, score, generate or review items, or code data) without addressing what
that means for the profession's norms, roles, training or accountability. Good validity or
fairness evidence for a method is not, by itself, a question about the profession.

Output, one line per item: `id,norms,confidence,rationale`, with norms 1 or 0, confidence `high`
or `low`, and a rationale of at most 20 words.
