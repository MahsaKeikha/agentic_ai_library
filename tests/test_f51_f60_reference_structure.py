from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SYSTEMS=["F51_digital_health_assistant","F52_clinical_trial_manager","F53_medical_device_development","F54_fda_documentation","F55_hospital_operations","F56_radiology_workflow","F57_pathology_review","F58_nursing_assistant","F59_caregiver_support","F60_rehabilitation_planning"]
REQUIRED=["AGENTS","TOOLS","SKILLS","orchestration","memory","state","schemas","prompts","config","safety","observability","evals","benchmarks","examples","tests","docs"]

def test_reference_layers_exist():
    for system in SYSTEMS:
        base=ROOT/"systems"/system
        assert base.exists(),system
        for layer in REQUIRED: assert (base/layer).exists(),f"{system}/{layer}"

def test_agents_tools_skills_are_real_files():
    for system in SYSTEMS:
        base=ROOT/"systems"/system
        assert len(list((base/"AGENTS").glob("*.py")))>=6
        assert len(list((base/"TOOLS").glob("*.py")))>=5
        assert len(list((base/"SKILLS").glob("*.py")))>=5
