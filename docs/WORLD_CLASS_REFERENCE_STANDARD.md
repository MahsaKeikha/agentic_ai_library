# World-Class Multi-Agent AI Reference Standard

This standard defines the minimum bar for every standalone system in the F30-F170 Agentic AI Library.

The objective is not to maximize repository count. The objective is to create a durable, auditable, reproducible engineering reference collection that researchers, engineers, educators, startups, enterprises, and public-interest teams can study and extend.

## 1. Standalone means standalone

Every F-number must have its own GitHub repository and must run without importing `agentic_ai_library` at runtime.

Each repository must include:

- a stable system identity and F-number
- multiple specialized agents with explicit responsibilities
- a real orchestrator coordinating those agents
- shared, traceable workflow state
- structured inputs and outputs
- deterministic offline execution
- tests
- CI
- examples
- architecture documentation
- evaluation criteria
- safety boundaries
- contribution guidance
- citation metadata
- version metadata

## 2. Reference architecture

Each repository follows this baseline structure:

```text
agentic_<system>/
├── README.md
├── LICENSE
├── CITATION.cff
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── pyproject.toml
├── run.py
├── src/
│   └── agentic_system/
│       ├── __init__.py
│       ├── agents.py
│       ├── orchestrator.py
│       ├── models.py
│       ├── policies.py
│       └── evaluation.py
├── examples/
│   ├── minimal_case.json
│   └── complete_case.json
├── tests/
│   ├── test_agents.py
│   ├── test_orchestrator.py
│   ├── test_safety.py
│   └── test_evaluation.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── AGENTS.md
│   ├── EVALUATION.md
│   ├── SAFETY.md
│   └── EXTENDING.md
└── .github/
    ├── workflows/tests.yml
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## 3. Multi-agent requirements

A repository is not considered multi-agent merely because several role names are listed.

Each system must demonstrate:

1. at least four specialized agents
2. distinct responsibility boundaries
3. an explicit orchestration sequence or graph
4. state passed between agents
5. evidence provenance or evidence-status tracking
6. conflict, missing-data, or escalation handling
7. a final synthesis or gatekeeping stage
8. human authorization before consequential action

## 4. Agent contract

Every agent should expose a predictable contract conceptually equivalent to:

```python
analyze(case, state) -> AgentResult
```

An `AgentResult` should identify:

- agent identity
- responsibility
- evidence used
- missing evidence
- assumptions
- findings
- confidence or evidence status
- risks
- recommended next action

Agents must not silently convert missing evidence into invented facts.

## 5. Orchestration contract

The orchestrator owns execution order, state updates, gates, and final synthesis.

At minimum it should preserve:

- `system_id`
- `system_name`
- `domain`
- `run_id`
- `started_at`
- `analyses`
- `evidence_gaps`
- `risks`
- `decision_log`
- `recommendation`
- `status`

The default implementation must run offline and deterministically so the system remains inspectable and teachable without paid APIs.

## 6. Safety and human authority

Approval must never erase unresolved risk.

Domain-specific blocking conditions must be explicit. Examples include unresolved clinical safety concerns, legal uncertainty, quality holds, hazardous physical execution, privacy or consent issues, rights/provenance issues, binding financial action, unsafe robotics operation, targeted political persuasion, or unsupported public claims.

The reference implementation separates decision support from consequential execution.

## 7. Evaluation

Every repository must contain both automated tests and a documented evaluation model.

Minimum evaluation dimensions:

- role separation
- evidence completeness
- traceability
- deterministic behavior
- orchestration correctness
- gate correctness
- failure handling
- safety-boundary adherence
- output schema stability

Repositories should include at least one adversarial or red-team test relevant to the domain.

## 8. Reproducibility

Every system must support:

```bash
python run.py
python run.py --case examples/complete_case.json
python -m pytest -q
```

A new reader should be able to clone the repository, run the offline example, understand the agent topology, and inspect the result without external credentials.

## 9. Documentation quality

The README is an engineering landing page, not marketing copy. It should answer:

- What problem does this system address?
- Why is a multi-agent architecture useful here?
- Which agents exist and why?
- How does information move through the system?
- What does the system produce?
- What are its limitations?
- How do I run and test it?
- How do I extend it?

`docs/ARCHITECTURE.md` must contain the execution flow and state model. `docs/EVALUATION.md` must explain what correctness means for the system. `docs/SAFETY.md` must define operational boundaries.

## 10. Open-source project hygiene

Every repository should include:

- semantic version beginning at `0.1.0`
- Apache-2.0 license unless a future project-specific licensing decision overrides it
- `CITATION.cff`
- `CONTRIBUTING.md`
- `SECURITY.md`
- changelog
- GitHub Actions on supported Python versions
- issue and pull request templates

## 11. Naming and discoverability

Repository names use stable descriptive slugs such as:

- `agentic_rag_engineering`
- `agentic_clinical_trial_manager`
- `agentic_robot_safety_validation`
- `agentic_enterprise_risk_manager`

The F-number remains stable in the README, citation metadata, package metadata, and master catalog.

## 12. Parent catalog contract

`agentic_ai_library` remains the canonical index. It should link to each standalone repository and record:

- F-number
- repository
- system name
- domain
- maturity/status
- CI status where practical
- version
- safety class

The umbrella repository should never claim a standalone repository exists until the repository is actually present on GitHub.

## 13. Maturity levels

Use a transparent maturity model:

- **Reference:** deterministic offline architecture, tests, docs, safety gates
- **Integrated:** optional external model/tool adapters available
- **Validated:** domain-specific benchmark/evaluation evidence added
- **Production-ready:** deployment, observability, security, and operational controls documented and tested

New F30-F170 repositories begin at **Reference**, not "production-ready".

## 14. Definition of done

A standalone F-system is complete only when:

- its GitHub repository exists
- it clones successfully
- its offline example runs
- all tests pass
- CI passes
- README and architecture docs accurately describe the implementation
- its agents are genuinely distinct
- its human gate and blocking conditions are tested
- the parent catalog links to the real repository
- no broken links remain

This standard is the quality gate for the F30-F170 standalone migration.
