# Source checks on claims in the panel materials

_Chair's notes for the session corpus, 6 October 2026. Each section checks one claim in the
panelists' materials (or in the session's own framing) against a public source, which is linked
and was read on 6 October 2026. The panelists' materials are unchanged; these notes sit beside
them so that claims can be contested on the record. Where a section gives an argument rather than
a sourced fact, it says so._

## 1. The ICLR 2025 peer-review study (relates to Briggs's example)

Briggs's statement and slides say that 27% of reviewers who got AI feedback revised, and that an
independent panel judged two-thirds (2/3) of the revised reviews better. His slide cites
Thakkar et al. 2025 and the published version in *Nature Machine Intelligence* (2026), via
*Science*.

What can be checked from public sources:

- **Revision rate.** 26.6% of reviewers who received feedback updated their reviews (rounded to
  27%), incorporating over 12,000 suggestions. The preprint, the ICLR blog and the published
  version agree on this.
- **Quality judgment, preprint version.** The preprint (arXiv:2504.09737) reports a blinded
  human evaluation of **100 selected examples**: updated reviews that received 3–4 feedback items
  and incorporated more than 60% of them. Annotators preferred the modified review **89% of the
  time**. The preprint also reports an **average incorporation rate of 67%**.
- **Quality judgment, published version.** *Nature Machine Intelligence* 8, 326–336 (2026). Its
  abstract says that "blinded evaluation confirmed that revised reviews receiving feedback were more
  informative". The full text is paywalled and was not checked here, so the published evaluation
  figure was not verified.

So the 27% matches every version. The quality figure differs by source: 89% on a selected subset
in the preprint, two-thirds in Briggs's citation of the published version. Either the published
evaluation differs from the preprint's, or the two-thirds figure reflects the 67% incorporation
rate. Briggs can say which.

Sources: https://arxiv.org/abs/2504.09737 ;
https://blog.iclr.cc/2025/04/15/leveraging-llm-feedback-to-enhance-review-quality/ ;
https://www.nature.com/articles/s42256-026-01188-x

## 2. Journal AI policy for peer reviewers in 2026 (relates to Briggs's claim)

Briggs's statement bounds its policy claim to "the 14 journals I checked". His slides give the
scan (3 NCME journals, 9 other measurement journals, 2 comparisons; 4 October 2026): 13 of 14
require authors to disclose generative AI use, 12 of 14 bar reviewers from putting manuscript
text into an AI tool, and none sets its own reviewer or editor rules (12 inherit them from seven
publishers). It also says "No
journal policy in our field addresses" a reviewer who revises after reading an AI critique.
Two large publishers' current reviewer policies:

- **Elsevier (updated June 2026).** "Reviewers should not upload a submitted manuscript or any part
  of it into an AI tool." Private AI tools are permitted for supporting tasks; a private tool is one
  where content is not retained beyond what the service needs and is not used for training or
  shared. Reviewers must disclose AI use, and "remain fully responsible and accountable for the
  content of their review reports."
- **Springer Nature.** Manuscript content "should not be uploaded" into public generative AI tools.
  "Confidentiality risks may be reduced when using secure or institutionally approved AI tools."
  Reviewers declare AI use, and AI "must not replace expert evaluation."

Both draw the distinction Briggs's proposal relies on: public tools versus private or
institutionally approved ones. Both keep the human reviewer accountable. Neither policy, as
quoted, says how a reviewer should attribute a change of judgment that an AI critique caused.

Sources: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals ;
https://www.springernature.com/gp/policies/editorial-policies/using-ai-in-peer-review

## 3. Dense observation and measurement inference (relates to Rijmen, slide 4 and brief §3)

_This section is an argument, not a sourced finding._

Rijmen argues that test theory samples behavior under standardized conditions because we cannot
observe people continuously, and that AI weakens that constraint. A counter-argument:

- Standardization exists for reasons beyond scarce observation: comparability across people,
  fairness of conditions, and defensibility of scores used for consequential decisions.
- Dense behavioral traces do not remove the need for inference. They bring new problems:
  - context dependence;
  - construct drift and construct-irrelevant variance;
  - missing data that is not random;
  - reactivity, when people behave differently because they are observed;
  - selection into what gets recorded;
  - comparability across settings;
  - privacy.

On this reading, AI-enabled observation changes the inference problem rather than eliminating it.
That fits Rijmen's own conclusion, that many observations of limited precision call for dynamic
measurement models, and extends it to validity and ethics.

## 4. "Computational or AI-related" versus "AI-specific" preparation (relates to Abulela)

Abulela et al.'s headline claim is about AI-related preparation. The evidence slide measures
"qualifying **computational or AI-related** coursework": 16 of 90 programs (17.8%). For job
advertisements it measures "at least one **computational or AI-related** area": 35 of 44 (79.5%).
The speaker notes say most qualifying coursework was in statistics programs, and list AI, machine
learning, NLP, data science, data mining and programming or computational skills.

The corpus does not include the study's sampling frame, collection dates, deduplication rules or
coding rubric. It also does not include a split between AI-specific and general computational
preparation. Questions about those belong to Abulela and co-authors.

## 5. The opening program chart (relates to the chair's framing)

The chair's opening slide summarizes the printed AIME-Con 2026 program (335 items). Each item was
coded on three independent yes/no questions by an AI coder. A blind second AI coder coded a
stratified sample of 98 items.

| Question | Items | Share | Agreement (n = 98) | κ |
|---|---|---|---|---|
| Builds AI into an assessment, learning or scoring product | 221 | 66% | 91% | 0.80 |
| Uses AI in measurement professionals' own methods and work | 131 | 39% | 97% | 0.94 |
| Asks what AI means for the profession itself (norms, roles, training, accountability) | 22 | 7% | 94% | 0.72 |

Things to know when contesting this chart:
- The rows overlap.
- Both coders are the same model family.
- The result depends on definitions. An earlier coding with mutually exclusive categories and
  a tie rule favoring "product" gave about 9:1 for products over professional work. With two
  independent questions it is about 1.7:1. The difference is mostly AI used as a psychometric
  method (difficulty prediction, calibration, item review), which the new coding counts as
  professional work.
- The chair's "10×" claim on the next slide is a conjecture about impact. It is not estimated
  from this coding.

Data, codebooks and agreement: https://dbetebenner.github.io/AIME_2026_Panel_Presentation/data/README.md

## 6. Evidence on AI-facilitated deliberation is mixed (relates to the session proposal, §10)

The session proposal says recent facilitation experiments find that participants prefer
AI-facilitated discussion while consensus does not improve. Two studies point in different
directions, in different designs:

- **Parisi et al. (FAccT 2026).** Real-time group deliberation on a charity allocation task,
  N = 879 across two studies. LLM facilitation did not significantly improve consensus. Participants
  still preferred facilitated discussion and cited inclusivity, but neither survey nor transcript
  measures of participation equity improved. Facilitators shifted some charity-level allocations by
  up to 5.5 percentage points.
- **Tessler et al. (*Science*, 2024).** An AI mediator (the "Habermas Machine") wrote group
  statements for UK participants discussing divisive issues, N = 5,734. Participants preferred the
  AI-written statements to human mediators' statements, groups were left less divided, and
  participants often converged on a shared position.

So the evidence is design-dependent. Perceived quality, participation, steering, grounding and
substantive outcomes are separate things to measure; success on one does not imply success on
another.

Sources: https://arxiv.org/abs/2605.14097 ;
https://deepmind.google/research/publications/224297/ ; Tessler et al., *Science* (2024),
doi:10.1126/science.adq2852

## 7. What lain "knows" (relates to how lain is described)

lain is built on a large language model, which carries knowledge from its pretraining. What the
session restricts is what counts as **evidence**:

- lain's evidence base is this corpus (the panelists' materials and these notes) and the live
  transcript;
- it has no open-web retrieval;
- a claim from the corpus needs a citation, a claim from the room needs a transcript reference,
  and anything else must be labeled inferred.

Pretrained knowledge may shape lain's reasoning, but it is not admissible as cited evidence.
