def adoption_snapshot(metrics):
    return {"metrics": metrics, "active_metrics": [k for k, v in metrics.items() if v is not None]}
