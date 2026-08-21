def plan_integration(priorities):
    return {"priorities": priorities, "workstreams": [{"name": p, "status": "planned"} for p in priorities]}
