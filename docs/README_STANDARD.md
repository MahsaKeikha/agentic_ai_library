# Atlas README Standard

Every README in the Multi-Agent AI Atlas should help a reader answer five questions without guessing:

1. What is this system for?
2. Which agents, tools, and controls shape the workflow?
3. What evidence supports its current status?
4. Where does automated authority stop?
5. Where can the reader inspect the architecture, tests, and public maturity record?

## Required positioning

Use the most specific claim supported by public evidence.

| Evidence state | Acceptable language | Language to avoid |
|---|---|---|
| Catalog entry | Reference architecture, catalog system | Verified, tested, production ready |
| Local package | Reference implementation, runnable example when confirmed | Deployed, operational in an enterprise |
| Demo Lab | Interactive synthetic simulation | Live production system |
| L3 registry entry | L3 Gold Standard reference architecture | Regulatory certification, guaranteed safe |
| External review | State the reviewer, scope, date, and evidence | Independently verified without a public record |
| Deployment | State only what the organization permits us to disclose | Proven at scale without documented evidence |

L3 is a project-defined engineering maturity designation. It is not a governmental, regulatory, legal, safety, security, or production certification.

## Required README sections

A full standalone system README should contain:

- purpose and decision-support scope
- architecture or agent-role summary
- workflow and human approval boundary
- repository structure
- installation and deterministic run instructions
- example input and output description
- test and evaluation instructions
- failure, refusal, and escalation behavior
- responsible-use limitations
- maturity and evidence link
- license, contribution, and citation information where applicable

Short catalog mirrors may point to a domain specification or standalone repository, but they must not imply a deeper implementation or maturity level than the files demonstrate.

## Voice and presentation

Write like an engineer explaining work to another engineer.

- Prefer concrete nouns and active verbs.
- State limits beside capabilities, not in a distant disclaimer.
- Avoid exaggerated adjectives and generic marketing language.
- Do not use unsupported superlatives such as definitive, proven, safest, or industry leading.
- Do not describe a score, portfolio selection, or catalog position as external validation.
- Use consistent F-numbers, system names, and domain labels.
- Keep navigation concise and useful.
- Do not use en dash or em dash characters.

## Public and private boundary

Public README files should explain the engineering principles, observable controls, and evidence standard clearly enough to support learning and informed evaluation. Organization-specific assessment methods, delivery tools, private training material, implementation playbooks, client workflows, and future commercial product direction remain private professional work.

## Canonical public links

- [Atlas home](https://mahsakeikha.github.io/agentic_ai_library/)
- [F01-F170 Architecture Atlas](https://mahsakeikha.github.io/agentic_ai_library/atlas.html)
- [10 Flagships](https://mahsakeikha.github.io/agentic_ai_library/flagships.html)
- [Interactive Demo Lab](https://mahsakeikha.github.io/agentic_ai_library/demo-lab.html)
- [Evidence and Maturity](https://mahsakeikha.github.io/agentic_ai_library/evidence.html)
- [Training](https://mahsakeikha.github.io/agentic_ai_library/training.html)
- [Field Guide](https://mahsakeikha.github.io/agentic_ai_library/atlas-book.html)

## Release review

Before merging a README change:

1. Verify every local and public link.
2. Compare maturity statements with `MATURITY_REGISTRY.md`.
3. Compare deployment and adoption statements with `ADOPTION_REGISTRY.md`.
4. Confirm that flagship language is presented as portfolio selection.
5. Confirm that Demo Lab language says synthetic simulation.
6. Remove unsupported certification, safety, production, and independent-review claims.
7. Check the text for en dash and em dash characters.
8. Read the introduction aloud and revise anything that sounds formulaic or impersonal.

This standard governs documentation quality. It does not assign maturity to a system.
