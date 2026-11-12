# Behavioral evaluation

`cases.json` contains synthetic requests with raw source text. Run each request with the installed skill and its relevant references. Do not show the evaluator an intended rewrite. Record the actual output and assess the following properties separately:

1. The result foregrounds an evidence-supported finding or decision without inventing significance, utility, facts, or citations.
2. Numbers, signs, units, comparators, populations, negation, and substantive claims survive.
3. Reused data, selected OOF scores, conditional interval coverage, null findings, and aggregate/subgroup trade-offs retain their meaning when present.
4. Needed contrast, causal uncertainty, deliberate author voice, and real reviewer responses remain.
5. Repetitive self-defence and artificial language are reduced; unchanged clear prose is acceptable.
6. Technical spans and notebook structure survive file edits. Run the notebook guard and review semantic accuracy separately.
7. Default output is final prose in the requested language and genre. Review mode follows the request.

There is no required wording or heading pattern. Score each property as pass, partial, or fail, and cite a concrete output passage for any failure. Treat a changed substantive claim as a failure even if the rewrite sounds better.

The deterministic unit suite validates notebook-preservation boundaries. It does not evaluate prose quality. Do not describe a static check as a behavioral run, or a fixture exercise as a test on real coursework.
