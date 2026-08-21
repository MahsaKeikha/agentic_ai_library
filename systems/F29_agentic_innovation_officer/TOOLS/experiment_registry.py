def register_experiment(name, hypothesis, metric, owner=None):
    return {"name": name, "hypothesis": hypothesis, "metric": metric, "owner": owner, "status": "registered"}
