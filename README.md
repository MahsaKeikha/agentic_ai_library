# Agentic AI Library

An open, practical collection of **runnable agentic AI patterns** for engineers, researchers, founders, and instructors.

This library is built to sit beside a serious book and a serious course. It is not a pile of toy prompts. Each entry is meant to be something you can clone, run offline, read in under fifteen minutes, and adapt with a clear human gate.

**GitHub umbrella (front door):**  
https://github.com/MahsaKeikha/agentic_ai_library

Pin this repository on your GitHub profile so it is the first place people land.

---

## Why this exists

Most agent demos stop at a clever chat loop. Real work needs more:

- specialized roles instead of one overloaded prompt
- tools with narrow jobs
- memory that survives a session
- an orchestrator that sequences work
- a human decision before anything is sent, applied, or submitted

This library packages those ideas as **flagship verticals** and **small core patterns** you can study and extend.

---

## What you get

| Layer | Meaning |
|--------|---------|
| **Flagship projects** | Full vertical demos (separate repos, linked below) |
| **Core catalog** | Focused examples under `catalog/core/` (C01 to C10 and growing) |
| **Templates** | Standard layout so new examples stay consistent |
| **Index** | Stable IDs for book and course references |

Everything is designed to run with **offline stand ins** first. Live model calls are optional when you set an API key.

---

## Flagship projects (full table)

Each flagship is its own GitHub repository. Local checklist: [flagships/README.md](flagships/README.md).

| ID | Repository | What it shows | Who it helps |
|----|------------|---------------|--------------|
| F01 | [agentic_book_writer](https://github.com/MahsaKeikha/agentic_book_writer) | Chapter pipeline: outline, research, draft, consistency, edit, ship gate | Authors, educators |
| F02 | [agentic_research_lab](https://github.com/MahsaKeikha/agentic_research_lab) | Literature intake, synthesis, questions, methods, citation audit, review | Researchers |
| F03 | [agentic_biotech_rd](https://github.com/MahsaKeikha/agentic_biotech_rd) | Program intake, landscape, hypotheses, design outline, compliance, critic. Not wet lab protocols. | Biotech planners |
| F04 | [agentic_tech_support](https://github.com/MahsaKeikha/agentic_tech_support) | Ticket intake, KB search, diagnosis, reply draft, escalation, policy, QA, send gate | Support teams |
| F05 | [agentic_online_shop](https://github.com/MahsaKeikha/agentic_online_shop) | Order cases, catalog, inventory, returns, risk notes, customer message, QA | E commerce |
| F06 | [agentic_debug_automation](https://github.com/MahsaKeikha/agentic_debug_automation) | Incident triage, logs, RCA, fix outline, automation sketch, verify, apply gate | SRE, automation |
| F07 | [agentic_software_design](https://github.com/MahsaKeikha/agentic_software_design) | Requirements, architecture, components, API, data model, trade offs, ADR, design review | Tech leads |
| F08 | [agentic_ceo_assistant](https://github.com/MahsaKeikha/agentic_ceo_assistant) | Daily briefing, priorities, inbox triage, metrics, decision memo, message draft, risks, CEO gate | Founders, Cos |
| F09 | [agentic_ai_safety](https://github.com/MahsaKeikha/agentic_ai_safety) | Safety review: scope, hazards, policy, eval plan, defensive red team, residual risk, incident, release gate | Safety, product |
| F10 | [agentic_phd_assistant](https://github.com/MahsaKeikha/agentic_phd_assistant) | PhD week loop: brief, reading, scholar notes, gaps, experiment sketch, outline, advisor pack, coach | PhD students |
| F11 | [agentic_account_manager](https://github.com/MahsaKeikha/agentic_account_manager) | Account snapshot, health, opportunity, risk, QBR, customer message, playbook, send gate | Account managers |
| F12 | [agentic_robotics_governance](https://github.com/MahsaKeikha/agentic_robotics_governance) | Robotics AI safety and governance: intake, hazards, policy, standards, release gates, incident, board brief, director gate | Safety directors |
| F13 | [agentic_qa_safety_manager](https://github.com/MahsaKeikha/agentic_qa_safety_manager) | QA and AI safety manager: scope, quality risks, safety hazards, test plan, eval gate, release, incident, manager gate | QA and safety managers |
| F14 | [agentic_client_inquiry_bot](https://github.com/MahsaKeikha/agentic_client_inquiry_bot) | Client email and chat inquiries: intake, channel, classify, KB, reply draft, escalate, policy, QA, send gate (with API error handling) | Support and success |

Keep IDs stable so the book and course can cite them.

---

## Core micro examples (live in this repo)

| ID | Folder | Teaches |
|----|--------|---------|
| C01 | `C01_tool_loop` | Single tool call, observe, stop |
| C02 | `C02_react_step` | Thought, act, observe |
| C03 | `C03_planner_executor` | Plan first, then execute |
| C04 | `C04_human_gate` | Default deny until explicit approve |
| C05 | `C05_memory_write` | Notes on disk between steps |
| C06 | `C06_checklist_editor` | Edits bound to a checklist |
| C07 | `C07_offline_client` | Same call shape offline or live |
| C08 | `C08_escalation_package` | Fixed handoff fields for humans |
| C09 | `C09_idempotent_tool` | Safe retries without double apply |
| C10 | `C10_eval_gate` | Fail closed on golden set regression |

```bash
cd catalog/core/C04_human_gate
python3 run.py --offline
```

---

## How every example is built

1. **Agents** with one job each  
2. **Tools** that are small and testable  
3. **File backed memory** for notes, drafts, and exports  
4. **Orchestrator** that runs a fixed pipeline  
5. **Human gate** before send, apply, ship, or approve  
6. **Offline mode** so CI and classrooms work without keys  

---

## Quick start

**Umbrella (micros):**

```bash
git clone https://github.com/MahsaKeikha/agentic_ai_library.git
cd agentic_ai_library/catalog/core/C01_tool_loop
python3 run.py --offline
```

**Any flagship:**

```bash
git clone https://github.com/MahsaKeikha/<flagship-repo>.git
cd <flagship-repo>
python3 run_*.py --offline
```

---

## For people using this in real work

**Do**

- Run offline first and read the outputs on disk  
- Treat drafts as drafts  
- Keep your own policy, legal, and safety review  
- Map examples to book or course using IDs (F01, C04, …)  

**Do not**

- Assume an agent may email customers, change production, or file regulatory claims without a human  
- Skip the ship or apply gate  
- Copy offline placeholder text into a paper or a customer reply  

---

## Roadmap

Long term aim: a **curated index of about 500 agentic patterns**.

| Phase | Focus |
|-------|--------|
| Now | Flagships F01 to F14, core C01 to C10, this umbrella |
| Next | Topic packs (memory, evals, security, workflows) |
| Ongoing | Course maps, book cross links, careful contributions |

---

## Book and course

Companion to the **AI Engineering Handbook** series and related teaching material by Mahsa Keikha.

---

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md). New micros should follow [templates/micro_example](templates/micro_example).

---

## Author

**Mahsa Keikha**

Building practical agentic systems for engineering, research, and leadership workflows.

---

## One line summary

**Agentic AI Library: runnable agent patterns with tools, memory, orchestration, and human gates, built to support real learning and real shipping.**
