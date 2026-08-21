# Reference Library Principles

The F30-F170 standalone migration is intended to create a credible engineering reference collection, not a collection of cloned boilerplate repositories.

## Principles

1. **Architecture before scale.** A small validated batch is more valuable than 141 superficially different repositories.
2. **Distinct agents, not renamed personas.** Role boundaries must correspond to meaningful subtasks and information responsibilities.
3. **Traceability over hidden magic.** Inputs, state, evidence gaps, risks, and gates should be inspectable.
4. **Offline-first reference execution.** Core examples should run without proprietary APIs so readers can reproduce behavior.
5. **Adapters are optional.** LLM providers, vector databases, external APIs, and enterprise tools can be added behind interfaces without becoming prerequisites for understanding the reference architecture.
6. **Evaluation is part of the product.** Each system should define what good performance means and how failures are detected.
7. **Safety is architecture.** Safety boundaries, human gates, and domain blockers belong in executable logic and tests, not only disclaimers.
8. **No maturity inflation.** Reference implementations are labeled as reference implementations until deployment, operational, security, and domain-validation requirements are actually met.
9. **Stable identifiers.** F-numbers remain stable so papers, books, courses, issues, and external references can cite a system consistently.
10. **Open contribution model.** The collection should make it easy for researchers and practitioners to propose new benchmarks, adapters, examples, and domain-specific improvements.

## What makes the collection useful globally

The library should let a reader compare the same engineering concepts across many domains: role decomposition, orchestration, shared state, evidence handling, gating, red teaming, evaluation, and human authority. Consistency makes cross-domain learning possible; domain-specific specialization prevents the systems from becoming generic wrappers.

The long-term value is a common vocabulary and reproducible set of reference architectures for multi-agent AI engineering.
