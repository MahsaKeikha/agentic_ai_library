# Library index

**Umbrella:** https://github.com/MahsaKeikha/agentic_ai_library

Local flagship list: [flagships/README.md](../flagships/README.md)

---

## Flagship verticals (F01 to F20)

| ID | Name | Description | Status |
|----|------|-------------|--------|
| F01 | agentic_book_writer | Chapter writing pipeline with ship gate | Live |
| F02 | agentic_research_lab | Academic research pipeline | Live |
| F03 | agentic_biotech_rd | Biotech R and D planning (documentation level) | Live |
| F04 | agentic_tech_support | Support tickets with QA and send gate | Live |
| F05 | agentic_online_shop | E commerce case handling | Live |
| F06 | agentic_debug_automation | Incident triage and automation sketches | Live |
| F07 | agentic_software_design | Software design package and ADR style notes | Live |
| F08 | agentic_ceo_assistant | Executive briefing and decision memo | Live |
| F09 | agentic_ai_safety | AI safety review and release gate | Live |
| F10 | agentic_phd_assistant | PhD weekly research assistant | Live |
| F11 | agentic_account_manager | Account health, QBR, client message | Live |
| F12 | agentic_robotics_governance | Robotics AI safety and governance director | Live |
| F13 | agentic_qa_safety_manager | QA and AI safety manager | Live |
| F14 | agentic_client_inquiry_bot | Email and chat client inquiries | Live |
| F15 | agentic_fullstack_web | Full stack web product and eng specs | Live |
| F16 | agentic_engineering_professor | Course, lecture, assignment, publish gate | Live |
| F17 | agentic_immigration_assistant | Immigration practice workflow (not legal advice) | Live |
| F18 | agentic_real_estate | Listing, showing, client update, compliance | Live |
| F19 | agentic_psychologist_assistant | Practice templates (not therapy or diagnosis) | Live |
| F20 | agentic_dating_advisor | Adult dating coach with safety and send gate | Live |

### Suggested GitHub URLs

| ID | URL |
|----|-----|
| F01 | https://github.com/MahsaKeikha/agentic_book_writer |
| F02 | https://github.com/MahsaKeikha/agentic_research_lab |
| F03 | https://github.com/MahsaKeikha/agentic_biotech_rd |
| F04 | https://github.com/MahsaKeikha/agentic_tech_support |
| F05 | https://github.com/MahsaKeikha/agentic_online_shop |
| F06 | https://github.com/MahsaKeikha/agentic_debug_automation |
| F07 | https://github.com/MahsaKeikha/agentic_software_design |
| F08 | https://github.com/MahsaKeikha/agentic_ceo_assistant |
| F09 | https://github.com/MahsaKeikha/agentic_ai_safety |
| F10 | https://github.com/MahsaKeikha/agentic_phd_assistant |
| F11 | https://github.com/MahsaKeikha/agentic_account_manager |
| F12 | https://github.com/MahsaKeikha/agentic_robotics_governance |
| F13 | https://github.com/MahsaKeikha/agentic_qa_safety_manager |
| F14 | https://github.com/MahsaKeikha/agentic_client_inquiry_bot |
| F15 | https://github.com/MahsaKeikha/agentic_fullstack_web |
| F16 | https://github.com/MahsaKeikha/agentic_engineering_professor |
| F17 | https://github.com/MahsaKeikha/agentic_immigration_assistant |
| F18 | https://github.com/MahsaKeikha/agentic_real_estate |
| F19 | https://github.com/MahsaKeikha/agentic_psychologist_assistant |
| F20 | https://github.com/MahsaKeikha/agentic_dating_advisor |

---

## Core patterns (C01 to C10)

| ID | Pattern | Status |
|----|---------|--------|
| C01 | Single tool call loop | Live |
| C02 | ReAct style thought and act | Live |
| C03 | Planner then executor | Live |
| C04 | Human approval gate | Live |
| C05 | Structured memory write | Live |
| C06 | Checklist driven editor | Live |
| C07 | Offline stand in client | Live |
| C08 | Escalation package | Live |
| C09 | Idempotent tool call | Live |
| C10 | Evaluation gate | Live |

Path: `catalog/core/<folder>/run.py`

---

## Notes for sensitive domains

- **F17** immigration: organizational aid only, not legal advice  
- **F19** psychologist assistant: templates only, not therapy or diagnosis  
- **F20** dating: adults only, consent and safety first  

Always keep human gates before client or public send.
