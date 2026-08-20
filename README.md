# Agentic AI Library

An open, practical collection of **runnable agentic AI patterns and multi-agent systems** for engineers, researchers, founders, educators, and operators.

This library is designed as a serious engineering reference: systems are expected to be runnable, evidence-aware, testable, and human-gated before consequential actions.

**GitHub umbrella:** https://github.com/MahsaKeikha/agentic_ai_library

---

## Why this exists

Real agent work needs more than a single chat loop:

- specialized roles
- narrow tools
- shared and persistent memory
- orchestration
- evaluation and guardrails
- human approval before consequential actions

---

## Library architecture

| Layer | Meaning |
|---|---|
| **F01 to F26 Flagships** | Standalone runnable repositories demonstrating complete vertical systems |
| **F27 to F170 Unified Systems** | Standardized packages developed inside this umbrella repository under `systems/` |
| **Core catalog** | Small reusable patterns under `catalog/core/` |
| **Templates** | Consistent layouts for new systems |
| **Index and roadmap** | Stable IDs for book, course, product, and commercial references |

This structure lets the collection scale without requiring 170 separately maintained repositories.

---

## Live standalone flagships (F01 to F26)

| ID | Repository | What it shows |
|---|---|---|
| F01 | [agentic_book_writer](https://github.com/MahsaKeikha/agentic_book_writer) | Book chapter pipeline with ship gate |
| F02 | [agentic_research_lab](https://github.com/MahsaKeikha/agentic_research_lab) | Academic research pipeline |
| F03 | [agentic_biotech_rd](https://github.com/MahsaKeikha/agentic_biotech_rd) | Biotech R and D planning |
| F04 | [agentic_tech_support](https://github.com/MahsaKeikha/agentic_tech_support) | Support tickets with send gate |
| F05 | [agentic_online_shop](https://github.com/MahsaKeikha/agentic_online_shop) | Shop case handling |
| F06 | [agentic_debug_automation](https://github.com/MahsaKeikha/agentic_debug_automation) | Incident debug and automation |
| F07 | [agentic_software_design](https://github.com/MahsaKeikha/agentic_software_design) | Senior software design package |
| F08 | [agentic_ceo_assistant](https://github.com/MahsaKeikha/agentic_ceo_assistant) | CEO daily briefing |
| F09 | [agentic_ai_safety](https://github.com/MahsaKeikha/agentic_ai_safety) | AI safety review |
| F10 | [agentic_phd_assistant](https://github.com/MahsaKeikha/agentic_phd_assistant) | PhD research week assistant |
| F11 | [agentic_account_manager](https://github.com/MahsaKeikha/agentic_account_manager) | B2B account management |
| F12 | [agentic_robotics_governance](https://github.com/MahsaKeikha/agentic_robotics_governance) | Robotics AI safety and governance |
| F13 | [agentic_qa_safety_manager](https://github.com/MahsaKeikha/agentic_qa_safety_manager) | QA and AI safety manager |
| F14 | [agentic_client_inquiry_bot](https://github.com/MahsaKeikha/agentic_client_inquiry_bot) | Email and chat client inquiries |
| F15 | [agentic_fullstack_web](https://github.com/MahsaKeikha/agentic_fullstack_web) | Full stack web design and engineering specs |
| F16 | [agentic_engineering_professor](https://github.com/MahsaKeikha/agentic_engineering_professor) | Engineering course and lecture prep |
| F17 | [agentic_immigration_assistant](https://github.com/MahsaKeikha/agentic_immigration_assistant) | Immigration workflow support, not legal advice |
| F18 | [agentic_real_estate](https://github.com/MahsaKeikha/agentic_real_estate) | Real estate listing and client updates |
| F19 | [agentic_psychologist_assistant](https://github.com/MahsaKeikha/agentic_psychologist_assistant) | Psychology practice templates, not therapy |
| F20 | [agentic_dating_advisor](https://github.com/MahsaKeikha/agentic_dating_advisor) | Adult dating coach with safety and send gate |
| F21 | [agentic_coo_assistant](https://github.com/MahsaKeikha/agentic_coo_assistant) | COO operations and KPI workflow |
| F22 | [agentic_cfo_assistant](https://github.com/MahsaKeikha/agentic_cfo_assistant) | CFO period brief, forecast, variance, and risk workflow |
| F23 | [agentic_board_advisor](https://github.com/MahsaKeikha/agentic_board_advisor) | Board package and governance workflow |
| F24 | [agentic_chief_of_staff](https://github.com/MahsaKeikha/agentic_chief_of_staff) | Executive priorities and follow-up workflow |
| F25 | [agentic_strategy_consultant](https://github.com/MahsaKeikha/agentic_strategy_consultant) | Competitive strategy and recommendation workflow |
| F26 | [agentic_venture_capital_analyst](https://github.com/MahsaKeikha/agentic_venture_capital_analyst) | Evidence-aware startup due diligence and investment memo workflow |

---

## Unified systems

F27 onward are standardized inside [`systems/`](systems/).

### Current build batch

| ID | System | Location |
|---|---|---|
| F27 | Agentic M&A Advisor | `systems/F27_agentic_ma_advisor/` |
| F28 | Agentic Startup Accelerator | `systems/F28_agentic_startup_accelerator/` |
| F29 | Agentic Innovation Officer | `systems/F29_agentic_innovation_officer/` |
| F30 | Agentic Corporate Governance | `systems/F30_agentic_corporate_governance/` |

Each package follows the engineering contract in [`systems/STANDARD.md`](systems/STANDARD.md): manifest, offline runner, example input, tests, evaluation criteria, responsible-use boundaries, and human approval logic.

---

## Core micro examples

C01 to C10 remain under `catalog/core/` and cover tool loops, ReAct steps, planner-executor patterns, human approval gates, memory, checklist editing, offline clients, escalation packages, idempotent tools, and evaluation gates.

```bash
cd catalog/core/C04_human_gate
python3 run.py --offline
```

---

## Responsible use

Sensitive-domain systems must preserve explicit scope limits, evidence discipline, and human review. No system should autonomously send, publish, file, transact, deploy capital, certify compliance, make clinical decisions, or take other consequential external actions without the required authorization and safeguards.

---

## Roadmap

The roadmap spans **F01 to F170**. F01 to F26 are standalone flagships. F27 onward are being standardized as unified system packages in this repository. Multi-agent organization concepts M01 to M06 remain part of the roadmap.

See [docs/ROADMAP.md](docs/ROADMAP.md).

---

## Author

**Mahsa Keikha**

Companion to the AI Engineering Handbook series and related courses.

**One line:** Runnable multi-agent systems with tools, memory, orchestration, evaluation, and human gates.
