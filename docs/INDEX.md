# Agentic AI Library Index

This is the stable catalog for the F01-F170 Agentic AI Library.

## Architecture

- **F01-F26:** live standalone flagship repositories
- **F27-F30:** dedicated unified packages under `systems/`
- **F31-F170:** domain-batch specifications, deterministic reference workflows, tests, and evaluation frameworks developed under `systems/`
- **C01-C10:** reusable core agentic patterns under `catalog/core/`

## Complete catalog

| Range | Domain | Systems |
|---|---|---|
| F01-F10 | Flagships I | Book Writer; Research Lab; Biotech R&D; Tech Support; Online Shop; Debug Automation; Software Design; CEO Assistant; AI Safety; PhD Assistant |
| F11-F20 | Flagships II | Account Manager; Robotics Governance; QA Safety Manager; Client Inquiry Bot; Fullstack Web; Engineering Professor; Immigration Assistant; Real Estate; Psychologist Assistant; Dating Advisor |
| F21-F30 | Executive & Leadership | COO; CFO; Board Advisor; Chief of Staff; Strategy Consultant; Venture Capital Analyst; M&A Advisor; Startup Accelerator; Innovation Officer; Corporate Governance |
| F31-F40 | AI Engineering | ML Engineer; MLOps Team; Data Engineering; Prompt Engineering; RAG Engineering; Multi-Agent Orchestrator; LLM Evaluator; AI Benchmark Suite; AI Product Manager; AI Infrastructure Architect |
| F41-F50 | Software Engineering | Mobile App Engineering; Cloud Architecture; DevOps; Kubernetes Operations; Cybersecurity SOC; Penetration Testing; API Engineering; Database Architecture; Embedded Systems; IoT Engineering |
| F51-F60 | Healthcare | Digital Health Assistant; Clinical Trial Manager; Medical Device Development; FDA Documentation; Hospital Operations; Radiology Workflow; Pathology Review; Nursing Assistant; Caregiver Support; Rehabilitation Planning |
| F61-F70 | Neuroscience | Parkinson Research; Dementia Care Planning; Hallucination Monitoring; EEG Analysis; Sleep Research; Neurotechnology Design; Brain Computer Interface; Cognitive Assessment; Aging Research; Biomarker Discovery |
| F71-F80 | Robotics | Industrial Robotics; Service Robotics; Medical Robotics; Autonomous Vehicles; Drone Operations; Humanoid Robot Design; Robot Safety Validation; Human-Robot Interaction; Swarm Robotics; Robotics Ethics |
| F81-F90 | Science | Physics Research Assistant; Quantum Computing; Materials Science; Chemistry Planning; Climate Science; Space Mission Design; Astronomy Research; Energy Systems; Nuclear Engineering; Scientific Literature Review |
| F91-F100 | Education | Professor Assistant; Curriculum Builder; Student Tutor; Exam Generator; STEM Laboratory Planner; University Research Office; Academic Integrity Checker; Grant Writer; Thesis Committee; Accreditation Manager |
| F101-F110 | Legal & Compliance | Contract Review; Corporate Compliance; Privacy Compliance; Intellectual Property; Patent Research; Employment Compliance; International Trade; Export Control; Healthcare Compliance; Regulatory Affairs |
| F111-F120 | Manufacturing | Manufacturing Engineer; Production Planner; Quality Engineer; Predictive Maintenance; Supply Chain Planner; Lean Manufacturing; Digital Twin Engineer; Factory Automation; Industrial Safety; Sustainability Engineer |
| F121-F130 | Marketing & Growth | Brand Strategist; Content Marketing; SEO Growth; Social Media Manager; Lifecycle Marketing; Paid Acquisition; Product Marketing; PR & Communications; Growth Experimentation; Customer Insights |
| F131-F140 | Creative & Media | Book Publishing; Screenwriting Studio; Music Production; Graphic Design; UX Design; Interior Design; Fashion Design; Architecture Studio; Game Design; Animation Studio |
| F141-F150 | Government & Public Sector | Smart City Planner; Emergency Management; Disaster Response; Public Health Planner; Transportation Planner; Environmental Compliance; Defense Policy Analyst; Public-Sector Intelligence Analyst; Election Information Reviewer; Policy Analyst |
| F151-F160 | Finance & Risk | Investment Research; Portfolio Manager; Quantitative Trading Research; Insurance Operations; Banking Assistant; Tax Planning; Enterprise Risk Manager; Treasury Operations; Credit Analyst; ESG Reporting |
| F161-F170 | Personal & Productivity | Life Planner; Personal Knowledge Manager; Career Coach; Resume Studio; Public Speaking Coach; Interview Coach; Language Tutor; Productivity Coach; Travel Planner; Habit Builder |

## Unified implementation files

The unified batches are represented by domain specification files, Python reference workflows, automated tests, and evaluation documents. Examples include `F31_F40_AI_ENGINEERING.md`, `ai_engineering_batch.py`, `F71_F80_ROBOTICS.md`, `robotics_batch.py`, and their corresponding tests/evaluation files.

## Core patterns C01-C10

C01 Single tool loop; C02 ReAct-style thought/action; C03 Planner-executor; C04 Human approval gate; C05 Structured memory; C06 Checklist editor; C07 Offline stand-in client; C08 Escalation package; C09 Idempotent tool call; C10 Evaluation gate.

## Responsible-use model

Human review remains required before consequential external action. Sensitive-domain systems retain domain-specific limitations, evidence requirements, stop conditions, escalation paths, and authorization gates. The reference library is an engineering and educational resource, not a substitute for qualified professional judgment.

See [`ROADMAP.md`](ROADMAP.md) for domain details and [`../systems/STANDARD.md`](../systems/STANDARD.md) for the unified engineering contract.
