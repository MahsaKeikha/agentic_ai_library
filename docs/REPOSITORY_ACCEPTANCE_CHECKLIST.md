# Standalone Repository Acceptance Checklist

Use this checklist for every F30-F170 repository before it is marked complete in the master catalog.

## Identity and discoverability

- [ ] Repository exists under the intended GitHub owner.
- [ ] Stable F-number appears in README and citation metadata.
- [ ] Repository name is descriptive and stable.
- [ ] Short GitHub description accurately explains the system.
- [ ] Relevant GitHub topics are assigned.
- [ ] Parent `agentic_ai_library` link is present.

## Multi-agent architecture

- [ ] At least four specialized agents exist.
- [ ] Agent responsibilities are meaningfully distinct.
- [ ] Orchestrator coordinates execution explicitly.
- [ ] Shared state is visible and traceable.
- [ ] Final synthesis/gatekeeper behavior exists.
- [ ] Agent outputs use a structured contract.

## Evidence and reasoning discipline

- [ ] Missing evidence is explicit.
- [ ] Assumptions are recorded.
- [ ] Evidence status/provenance is preserved.
- [ ] Conflicting inputs are surfaced rather than silently resolved.
- [ ] Open risks remain visible in the final result.

## Safety and human authority

- [ ] Domain-specific boundaries are documented.
- [ ] Consequential external actions require explicit authorization.
- [ ] Approval cannot erase unresolved blockers.
- [ ] At least one domain-specific red-team test exists.
- [ ] Sensitive-domain escalation behavior is tested where applicable.

## Reproducibility

- [ ] Fresh clone succeeds.
- [ ] `python run.py` succeeds offline.
- [ ] Minimal example succeeds.
- [ ] Complete example succeeds.
- [ ] `python -m pytest -q` passes.
- [ ] Python support range matches CI.

## CI and engineering hygiene

- [ ] GitHub Actions exists.
- [ ] CI is green on supported Python versions.
- [ ] `pyproject.toml` contains version and project metadata.
- [ ] `.gitignore` is present.
- [ ] No secrets, tokens, personal credentials, or machine-specific paths are committed.

## Documentation

- [ ] README explains the problem and why multi-agent architecture is used.
- [ ] README includes quick start and examples.
- [ ] `docs/ARCHITECTURE.md` explains flow and state.
- [ ] `docs/AGENTS.md` documents each agent contract.
- [ ] `docs/EVALUATION.md` explains correctness and metrics.
- [ ] `docs/SAFETY.md` explains boundaries and blocking conditions.
- [ ] `docs/EXTENDING.md` explains how to add tools, agents, or adapters.
- [ ] All internal and external links resolve.

## Open-source reference quality

- [ ] LICENSE is present.
- [ ] CITATION.cff is present.
- [ ] CONTRIBUTING.md is present.
- [ ] SECURITY.md is present.
- [ ] CHANGELOG.md is present.
- [ ] Pull request template is present.
- [ ] Issue templates are present.

## Catalog integration

- [ ] Master catalog points to the actual repository URL.
- [ ] Launcher points to the actual repository URL.
- [ ] Maturity level is accurate.
- [ ] Version is recorded.
- [ ] CI status is not misrepresented.
- [ ] The umbrella repository does not retain a contradictory status statement.

## Acceptance rule

A repository is not marked complete until every applicable item above is checked. Repositories with missing evidence, broken CI, broken links, or only superficial role separation remain **Reference Draft** and are not promoted to the verified catalog.
