# Paper 1 submission package

## Manuscript

**Anticipatory Supervisory Control of Protected Actions in Tool-Using Multi-Agent AI**

Author: Mahsa Keikha

Affiliation: Connected Care LLC, California, USA

Primary target: 2027 American Control Conference, contributed paper.

## Scientific contribution

This paper does not claim that supervisory control, runtime assurance, authorization gates, or human review are individually new. Its scoped contribution is a discrete-event formulation for tool-using multi-agent workflows in which authority and evidence invalidations are explicit uncontrollable events, protected-action violations are forbidden states, and successful completion plus human review are marked outcomes.

The paper introduces:

1. The Authority and Evidence Task Automaton, AETA.
2. The Authority and Evidence Supervisory Controller, AESC.
3. The precursor-vulnerability set, which identifies states admitted by pointwise protection but excluded from the maximal safe, uncontrollable-closed, nonblocking winning set.
4. A pointwise-sufficiency theorem and anticipatory precursor-suppression corollary.
5. Four reproducible Atlas-derived synthetic workflow abstractions.
6. An independent brute-force implementation oracle and finite-state scaling study.

The claims are model-level guarantees conditional on the supplied finite-state abstraction. They are not claims of real-world deployment safety.

## Verified evidence snapshot

- 1,200,000 seeded case-study rollouts.
- Four Atlas-derived synthetic workflow abstractions.
- Zero modeled AESC violations in the four abstractions.
- Zero modeled AESC deadlocks in the four abstractions.
- 5,000 brute-force oracle comparisons with zero winning-set mismatches.
- Four regression tests passing.
- Scaling measurements through 2,000-state random feasible plants.
- Separate dense-random structural stress survey, explicitly not treated as a real-world prevalence estimate.

## Reproduce experiments

From the C01_acc2027 directory:

    python code/run_experiments.py --runs 100000 --seed 20260919 --replicates 30 --survey-plants 100 --out results
    python code/verify_synthesis.py --plants 5000 --seed 20260919 --out results/exhaustive_oracle_summary.csv
    python -m pytest -q tests

## Submission format

PaperPlaza supplies the official ieeeconf class in its author kit. The final local package contains the ACC source variant and a compliance PDF. The PDF is six pages, US Letter, PDF 1.4, under 2 MB, with embedded fonts and no Type 3 fonts. It must still be passed through PaperPlaza's own PDF Test before submission.

## Punctuation QA

The final manuscript source and rendered PDF were scanned for Unicode en dash and em dash characters. Neither is present. The manuscript source also contains no double-hyphen dash construction.

## AI tool disclosure

The manuscript includes a specific disclosure because ACC 2027 requires transparent disclosure and citation of LLM tools used for research, writing or editing, artwork, or synthetic data. The scientific figures are generated from code and recorded results, not from an image-generation model.
