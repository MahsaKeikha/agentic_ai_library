# Agentic AI Library Maturity Registry

This registry records evidence-backed maturity promotions for F01-F170. A repository appears as L3 only after satisfying the Gold Standard acceptance gate on its standalone repository.

| ID | System | Maturity | Version | Verified main commit | CI evidence | Benchmark evidence |
|---|---|---|---|---|---|---|
| F40 | Agentic AI Infrastructure Architect | **L3 Gold Standard** | **1.0.0** | `f7411a7e6a2d15287555752e3dc9b10f387720dd` | Gold Standard CI run `32539482014` and compatibility CI run `32539481959`, all Python 3.10/3.11/3.12 jobs green | Held-out suite 8/8 passed, pass rate 1.0; source artifact `f40-heldout-results`; results recorded in standalone `benchmarks/RESULTS.md` |

## Promotion policy

L3 status is evidence-backed and can be suspended if required CI later fails, a high-severity security issue remains unresolved, critical-path placeholder logic is introduced, reproducibility breaks, or the documented benchmark/safety claims no longer match implementation.

The absence of a repository from the L3 table does not imply failure. It means that repository has not yet completed the L3 promotion process under the current Gold Standard.
