# F111 to F120: Manufacturing Systems

This batch adds ten manufacturing and industrial operations multi-agent reference systems. They support engineering and operations decisions and do not autonomously command production equipment.

| ID | System | Core roles | Primary output |
|---|---|---|---|
| F111 | Agentic Manufacturing Engineer | Process Analyst, Equipment Engineer, Quality Agent, Safety Reviewer, Cost Analyst, Change Reviewer | Manufacturing engineering package |
| F112 | Agentic Production Planner | Demand Analyst, Capacity Planner, Scheduler, Constraint Agent, Inventory Reviewer, Plan Gatekeeper | Production plan and constraint report |
| F113 | Agentic Quality Engineer | Requirement Analyst, Inspection Planner, SPC Analyst, Nonconformance Agent, CAPA Reviewer, Release Gatekeeper | Quality and corrective-action package |
| F114 | Agentic Predictive Maintenance | Asset Analyst, Condition Agent, Failure-Mode Analyst, Maintenance Planner, Reliability Reviewer, Work-Order Gatekeeper | Maintenance recommendation package |
| F115 | Agentic Supply Chain Planner | Demand Agent, Supplier Analyst, Inventory Agent, Logistics Planner, Risk Reviewer, Sourcing Gatekeeper | Supply-chain plan and risk register |
| F116 | Agentic Lean Manufacturing | Value-Stream Analyst, Waste Analyst, Flow Designer, Kaizen Planner, Metrics Agent, Change Reviewer | Lean improvement plan |
| F117 | Agentic Digital Twin Engineer | System Modeler, Data Interface Agent, Calibration Analyst, Simulation Reviewer, Validation Agent, Deployment Gatekeeper | Digital-twin model and validation package |
| F118 | Agentic Factory Automation | Requirements Agent, Controls Architect, Integration Agent, Safety Reviewer, Verification Agent, Commissioning Gatekeeper | Factory automation design package |
| F119 | Agentic Industrial Safety | Hazard Analyst, Risk Assessor, Control Planner, Procedure Reviewer, Training Agent, Safety Gatekeeper | Industrial safety assessment |
| F120 | Agentic Sustainability Engineer | Resource Analyst, Energy Agent, Waste/Emissions Analyst, Lifecycle Reviewer, Economics Agent, Improvement Gatekeeper | Manufacturing sustainability plan |

## Operational boundary

The reference workflows do not issue PLC commands, alter safety interlocks, start or stop machinery, change production recipes, approve product release, or create binding supplier commitments. Real-world changes require site-specific verification and authorized human approval.
