# Methods: two-dimension and norms coding of the AIME-Con 2026 program

Everything needed to inspect or reproduce the opening chart (see `../README.md` for the results).

| File | What it is |
|---|---|
| `codebook-2d.md` | Codebook v2: `product` and `profession`, the coders' only instructions |
| `codebook-norms.md` | Codebook v2.1: the `norms` question |
| `items-text.jsonl` | The 335 program items as the coders saw them: id, session, title, abstract text |
| `sessions-text.jsonl` | The 83 sessions as the coders saw them |
| `coder1-items.csv`, `coder1-norms.csv`, `coder1-sessions.csv` | Primary AI coder, blind to the v1 coding |
| `second-coder-sample.json` | The blind stratified sample of 98 items (design and seed) |
| `coder2-sample.csv`, `coder2-norms.csv` | Second AI coder, blind to the primary coder |
| `agreement.json` | Agreement, Cohen's κ and confusion tables; also how v1 codes map to v2 cells |
| `audit-2d.md` | The chair's audit sheet: coder disagreements and items whose classification moved |
| `merge.py` | Rebuilds `../program-items-coded.csv` and the norms agreement |

Both coders are instances of the same model family (Claude). Agreement therefore shows the
codebook can be applied consistently; it is not independent human judgment.
