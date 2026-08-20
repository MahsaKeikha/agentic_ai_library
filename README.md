# Agentic AI Library

An open, practical collection of **runnable agentic AI patterns** for engineers, researchers, founders, educators, and operators.

This library is built to sit beside a serious book and a serious course. Each entry is meant to be something you can clone, run offline, read quickly, and adapt with a clear human gate.

**GitHub umbrella (front door):**  
https://github.com/MahsaKeikha/agentic_ai_library

Pin this repository on your GitHub profile so it is the first place people land.

---

## Why this exists

Real agent work needs more than a single chat loop:

- specialized roles
- narrow tools
- memory that survives a session
- an orchestrator
- a human decision before send, apply, publish, or file

---

## What you get

| Layer | Meaning |
|--------|---------|
| **Flagship projects** | Full vertical demos (separate repos) |
| **Core catalog** | Small patterns under `catalog/core/` (C01 to C10) |
| **Templates** | Consistent layout for new examples |
| **Index** | Stable IDs for book and course |

Offline first. Live models optional with an API key.

---

## Flagship projects (F01 to F20)

| ID | Repository | What it shows |
|----|------------|---------------|
| F01 | [agentic_book_writer](https://github.com/MahsaKeikha/agentic_book_writer) | Book chapter pipeline with ship gate |
| F02 | [agentic_research_lab](https://github.com/MahsaKeikha/agentic_research_lab) | Academic research pipeline |
| F03 | [agentic_biotech_rd](https://github.com/MahsaKeikha/agentic_biotech_rd) | Biotech R and D planning (not wet lab) |
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
| F17 | [agentic_immigration_assistant](https://github.com/MahsaKeikha/agentic_immigration_assistant) | Immigration practice workflow (not legal advice) |
| F18 | [agentic_real_estate](https://github.com/MahsaKeikha/agentic_real_estate) | Real estate listing and client updates |
| F19 | [agentic_psychologist_assistant](https://github.com/MahsaKeikha/agentic_psychologist_assistant) | Psychology practice templates (not therapy) |
| F20 | [agentic_dating_advisor](https://github.com/MahsaKeikha/agentic_dating_advisor) | Adult dating coach with safety and send gate |

Local link list: [flagships/README.md](flagships/README.md)

---

## Core micro examples (in this repo)

| ID | Folder | Teaches |
|----|--------|---------|
| C01 | `C01_tool_loop` | Tool call loop |
| C02 | `C02_react_step` | Thought, act, observe |
| C03 | `C03_planner_executor` | Plan then execute |
| C04 | `C04_human_gate` | Human approval gate |
| C05 | `C05_memory_write` | File memory |
| C06 | `C06_checklist_editor` | Checklist driven edits |
| C07 | `C07_offline_client` | Offline stand in client |
| C08 | `C08_escalation_package` | Escalation handoff |
| C09 | `C09_idempotent_tool` | Idempotent tools |
| C10 | `C10_eval_gate` | Evaluation gate |

```bash
cd catalog/core/C04_human_gate
python3 run.py --offline
```

---

## Quick start

```bash
git clone https://github.com/MahsaKeikha/agentic_ai_library.git
cd agentic_ai_library/catalog/core/C01_tool_loop
python3 run.py --offline
```

Clone any flagship separately and run its `run_*.py --offline`.

---

## Responsible use

Many flagships are **workflow assistants**, not professional licenses.

- Immigration assistant is **not legal advice**
- Psychologist assistant is **not therapy or diagnosis**
- Real estate and dating tools need human judgment and local rules
- Always keep the human gate before send, publish, or file

---

## Roadmap

Curated growth toward about **500** agentic patterns (flagships for depth, micros for breadth). Quality over empty repos.

---

## Author

**Mahsa Keikha**

Companion to the AI Engineering Handbook series and related courses. https://a.co/d/0cXYwuHR and https://a.co/d/02Inzh4Q

**One line:** Runnable agent patterns with tools, memory, orchestration, and human gates.

## Full roadmap

See [docs/ROADMAP.md](docs/ROADMAP.md) for F21 to F170 and multi agent organizations M01 to M06.
