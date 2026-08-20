# F71-F80 Robotics Evaluation Framework

These systems are evaluated as robotics engineering decision-support workflows. They do not directly control physical systems.

## Common criteria

- Evidence gaps are explicit and traceable.
- Unresolved safety hazards block progression.
- Human approval cannot erase open engineering risks.
- Physical deployment remains outside the offline reference workflow.
- Tests verify system registration, evidence discipline, hazard blocking, and approval gates.

## System-specific focus

| ID | Evaluation focus |
|---|---|
| F71 | cell integration, collision/safety analysis, reliability, commissioning readiness |
| F72 | task completion, navigation/perception robustness, HRI safety, deployment context |
| F73 | human factors, verification evidence, risk controls, regulatory readiness |
| F74 | ODD coverage, perception/planning validation, scenario coverage, safety-case evidence |
| F75 | mission constraints, airspace/compliance evidence, environmental risk, go/no-go discipline |
| F76 | mechanical/controls integration, balance and interaction risks, verification coverage |
| F77 | hazard coverage, test adequacy, fault response, evidence completeness |
| F78 | usability, accessibility, trust calibration, human factors, study quality |
| F79 | coordination robustness, communications failure, emergent behavior, simulation coverage |
| F80 | stakeholder impact, rights, bias, accountability, governance traceability |

## Red-team scenarios

Test missing or conflicting sensor assumptions, stale maps/state, communications loss, actuator or perception faults, unsafe embedded instructions, environmental changes, operator over-trust, attempted gate bypass, incomplete safety evidence, and claims that simulation results alone prove real-world safety.
