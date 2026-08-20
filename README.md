# Agentic AI Library

A practical engineering library of **170 agentic AI and multi-agent systems** spanning executive operations, AI engineering, software, healthcare, neuroscience, robotics, science, education, legal and compliance, manufacturing, marketing, creative work, public-sector workflows, finance and risk, and personal productivity.

The goal is not to collect prompt demos. The library is organized around reusable engineering principles: specialized roles, explicit state, evidence discipline, orchestration, evaluation, failure handling, and human approval before consequential actions.

## Current status

**F01-F170 are now represented in the library and integrated into `main`.**

- F01-F26 are standalone flagship repositories.
- F27-F170 are organized through the unified `systems/` architecture in this repository.
- C01-C10 provide small reusable core agentic patterns.
- Automated tests run through GitHub Actions on pushes and pull requests to `main`.

See [`docs/INDEX.md`](docs/INDEX.md) for the full catalog and [`docs/ROADMAP.md`](docs/ROADMAP.md) for domain-level organization.

## Library at a glance

| Range | Domain | Architecture |
|---|---|---|
| F01-F26 | Standalone flagship systems | Dedicated repositories |
| F27-F30 | Executive and leadership | Unified systems |
| F31-F40 | AI engineering | Unified batch |
| F41-F50 | Software engineering | Unified batch |
| F51-F60 | Healthcare | Unified batch |
| F61-F70 | Neuroscience | Unified batch |
| F71-F80 | Robotics | Unified batch |
| F81-F90 | Science | Unified batch |
| F91-F100 | Education | Unified batch |
| F101-F110 | Legal and compliance | Unified batch |
| F111-F120 | Manufacturing | Unified batch |
| F121-F130 | Marketing and growth | Unified batch |
| F131-F140 | Creative and media | Unified batch |
| F141-F150 | Government and public sector | Unified batch |
| F151-F160 | Finance and risk | Unified batch |
| F161-F170 | Personal and productivity | Unified batch |

## Engineering philosophy

A useful multi-agent system needs more than several personas talking to one another. Unified systems are designed around:

- specialized agents with narrow responsibilities
- structured inputs and outputs
- shared or traceable workflow state
- explicit treatment of missing evidence and uncertainty
- deterministic offline reference paths where practical
- domain-specific evaluation criteria
- failure, escalation, and stop conditions
- human approval gates for consequential actions
- responsible-use boundaries appropriate to the domain

The shared engineering contract is documented in [`systems/STANDARD.md`](systems/STANDARD.md).

## Standalone flagships F01-F26

| ID | Repository | Focus |
|---|---|---|
| F01 | [agentic_book_writer](https://github.com/MahsaKeikha/agentic_book_writer) | Book chapter pipeline with ship gate |
| F02 | [agentic_research_lab](https://github.com/MahsaKeikha/agentic_research_lab) | Academic research pipeline |
| F03 | [agentic_biotech_rd](https://github.com/MahsaKeikha/agentic_biotech_rd) | Biotech R&D planning |
| F04 | [agentic_tech_support](https://github.com/MahsaKeikha/agentic_tech_support) | Support workflow with send gate |
| F05 | [agentic_online_shop](https://github.com/MahsaKeikha/agentic_online_shop) | Online-shop case handling |
| F06 | [agentic_debug_automation](https://github.com/MahsaKeikha/agentic_debug_automation) | Incident debugging and automation |
| F07 | [agentic_software_design](https://github.com/MahsaKeikha/agentic_software_design) | Senior software design package |
| F08 | [agentic_ceo_assistant](https://github.com/MahsaKeikha/agentic_ceo_assistant) | CEO daily briefing |
| F09 | [agentic_ai_safety](https://github.com/MahsaKeikha/agentic_ai_safety) | AI safety review |
| F10 | [agentic_phd_assistant](https://github.com/MahsaKeikha/agentic_phd_assistant) | PhD research-week assistant |
| F11 | [agentic_account_manager](https://github.com/MahsaKeikha/agentic_account_manager) | B2B account management |
| F12 | [agentic_robotics_governance](https://github.com/MahsaKeikha/agentic_robotics_governance) | Robotics AI safety and governance |
| F13 | [agentic_qa_safety_manager](https://github.com/MahsaKeikha/agentic_qa_safety_manager) | QA and AI safety management |
| F14 | [agentic_client_inquiry_bot](https://github.com/MahsaKeikha/agentic_client_inquiry_bot) | Client inquiry workflow |
| F15 | [agentic_fullstack_web](https://github.com/MahsaKeikha/agentic_fullstack_web) | Full-stack web engineering specs |
| F16 | [agentic_engineering_professor](https://github.com/MahsaKeikha/agentic_engineering_professor) | Engineering course and lecture preparation |
| F17 | [agentic_immigration_assistant](https://github.com/MahsaKeikha/agentic_immigration_assistant) | Immigration workflow support, not legal advice |
| F18 | [agentic_real_estate](https://github.com/MahsaKeikha/agentic_real_estate) | Real-estate workflow support |
| F19 | [agentic_psychologist_assistant](https://github.com/MahsaKeikha/agentic_psychologist_assistant) | Psychology-practice templates, not therapy |
| F20 | [agentic_dating_advisor](https://github.com/MahsaKeikha/agentic_dating_advisor) | Adult dating coaching with safety/send gate |
| F21 | [agentic_coo_assistant](https://github.com/MahsaKeikha/agentic_coo_assistant) | COO operations and KPI workflow |
| F22 | [agentic_cfo_assistant](https://github.com/MahsaKeikha/agentic_cfo_assistant) | CFO forecast, variance, and risk workflow |
| F23 | [agentic_board_advisor](https://github.com/MahsaKeikha/agentic_board_advisor) | Board package and governance workflow |
| F24 | [agentic_chief_of_staff](https://github.com/MahsaKeikha/agentic_chief_of_staff) | Executive priorities and follow-up |
| F25 | [agentic_strategy_consultant](https://github.com/MahsaKeikha/agentic_strategy_consultant) | Competitive strategy workflow |
| F26 | [agentic_venture_capital_analyst](https://github.com/MahsaKeikha/agentic_venture_capital_analyst) | Evidence-aware venture due diligence |

## Unified systems F27-F170

| Range | Domain | Representative systems |
|---|---|---|
| F27-F30 | Executive | M&A Advisor, Startup Accelerator, Innovation Officer, Corporate Governance |
| F31-F40 | AI Engineering | ML Engineer, MLOps, Data Engineering, Prompt Engineering, RAG, Orchestration, LLM Evaluation |
| F41-F50 | Software | Mobile, Cloud, DevOps, Kubernetes, SOC, API, Database, Embedded, IoT |
| F51-F60 | Healthcare | Digital Health, Clinical Trials, Medical Devices, FDA Documentation, Hospital Operations, Caregiver Support |
| F61-F70 | Neuroscience | Parkinson, Dementia, EEG, Sleep, Neurotechnology, BCI, Aging, Biomarkers |
| F71-F80 | Robotics | Industrial, Service, Medical, AV, Drone, Humanoid, Safety, HRI, Swarm, Ethics |
| F81-F90 | Science | Physics, Quantum, Materials, Chemistry, Climate, Space, Astronomy, Energy, Nuclear |
| F91-F100 | Education | Professor, Curriculum, Tutor, Exams, STEM Lab, Grants, Thesis, Accreditation |
| F101-F110 | Legal & Compliance | Contracts, Privacy, IP, Patents, Employment, Trade, Export, Regulatory Affairs |
| F111-F120 | Manufacturing | Manufacturing, Production, Quality, Maintenance, Supply Chain, Digital Twin, Automation, Safety |
| F121-F130 | Marketing & Growth | Brand, Content, SEO, Social, Lifecycle, Acquisition, Product Marketing, PR, Growth |
| F131-F140 | Creative & Media | Publishing, Screenwriting, Music, Graphic Design, UX, Architecture, Games, Animation |
| F141-F150 | Public Sector | Smart City, Emergency, Disaster, Public Health, Transport, Environment, Policy |
| F151-F160 | Finance & Risk | Investment Research, Portfolio, Quant Research, Insurance, Banking, Tax, Risk, Treasury |
| F161-F170 | Personal & Productivity | Life Planning, Knowledge, Career, Resume, Speaking, Interview, Language, Travel, Habits |

## Core reusable patterns C01-C10

The `catalog/core/` folder contains compact reusable patterns for tool loops, ReAct-style steps, planner-executor workflows, human approval gates, structured memory, checklist editing, offline stand-in clients, escalation packages, idempotent tool calls, and evaluation gates.

```bash
cd catalog/core/C04_human_gate
python3 run.py --offline
```

## Testing

The repository includes automated tests for the unified batches. GitHub Actions runs the test suite against Python 3.10, 3.11, and 3.12 on pushes and pull requests to `main`.

Local test command:

```bash
python -m pip install pytest
python -m pytest -q
```

## Safety and responsible use

The library intentionally separates decision support from consequential execution. Sensitive systems preserve appropriate scope limits and qualified review. Reference workflows should not silently invent missing facts or autonomously perform consequential actions such as clinical decisions, legal certification, financial transactions, physical robot control, industrial equipment commands, targeted voter persuasion, binding public decisions, or external submissions without appropriate authorization and safeguards.

## Repository structure

```text
agentic_ai_library/
├── .github/workflows/tests.yml
├── README.md
├── catalog/core/
├── docs/
│   ├── INDEX.md
│   └── ROADMAP.md
├── flagships/
├── systems/
│   ├── STANDARD.md
│   ├── F27_agentic_ma_advisor/
│   ├── F28_agentic_startup_accelerator/
│   ├── F29_agentic_innovation_officer/
│   ├── F30_agentic_corporate_governance/
│   ├── domain specifications
│   ├── deterministic reference workflows
│   ├── evaluation frameworks
│   └── tests/
└── templates/
```

## Author

**Mahsa Keikha**

Companion engineering library for the **AI Engineering Handbook Series** and related educational work.

**One line:** 170 agentic AI systems built around tools, state, orchestration, evidence, evaluation, safety boundaries, and human gates.
