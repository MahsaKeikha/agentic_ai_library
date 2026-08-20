# F71 to F80: Robotics Systems

This batch adds ten robotics-focused multi-agent reference systems. These are engineering decision-support workflows, not autonomous physical-control systems.

| ID | System | Core roles | Primary output |
|---|---|---|---|
| F71 | Agentic Industrial Robotics | Cell Analyst, Motion Planner, Integration Engineer, Safety Reviewer, Reliability Agent, Commissioning Reviewer | Robot-cell engineering package |
| F72 | Agentic Service Robotics | Task Analyst, Interaction Designer, Navigation Reviewer, Perception Agent, Safety Agent, Deployment Reviewer | Service-robot deployment plan |
| F73 | Agentic Medical Robotics | Clinical Workflow Analyst, Systems Engineer, Human Factors Agent, Verification Agent, Risk Manager, Regulatory Reviewer | Medical-robot development package |
| F74 | Agentic Autonomous Vehicles | ODD Analyst, Perception Reviewer, Planning Reviewer, Validation Agent, Safety Case Agent, Release Gatekeeper | AV validation and safety package |
| F75 | Agentic Drone Operations | Mission Planner, Airspace Reviewer, Payload Analyst, Weather/Risk Agent, Compliance Reviewer, Go-No-Go Gatekeeper | Drone mission review package |
| F76 | Agentic Humanoid Robot Design | Requirements Agent, Mechanical Architect, Controls Agent, Perception/HRI Agent, Safety Reviewer, Verification Planner | Humanoid system design package |
| F77 | Agentic Robot Safety Validation | Hazard Analyst, Test Designer, Fault Injection Reviewer, Safety Metrics Agent, Evidence Auditor, Approval Gatekeeper | Robot safety validation report |
| F78 | Agentic Human-Robot Interaction | Context Analyst, Interaction Designer, Accessibility Agent, Human Factors Reviewer, Trust/Safety Agent, Study Planner | HRI design and evaluation plan |
| F79 | Agentic Swarm Robotics | Mission Decomposer, Coordination Architect, Communications Agent, Resilience Analyst, Simulation Reviewer, Safety Gatekeeper | Swarm coordination and simulation plan |
| F80 | Agentic Robotics Ethics | Stakeholder Analyst, Rights/Impact Agent, Bias Reviewer, Safety/Ethics Agent, Governance Reviewer, Decision Recorder | Robotics ethics and governance assessment |

## Safety boundary

The offline reference workflows do not issue actuator commands, control physical robots, bypass interlocks, or authorize real-world operation. Physical deployment requires domain-specific engineering verification, applicable regulatory/compliance review, and explicit qualified-human authorization.

## Shared engineering requirements

Each system must preserve explicit evidence status, traceable state, deterministic offline examples, system-specific evaluation criteria, failure/escalation paths, and human gates before physical deployment or safety-critical action.
