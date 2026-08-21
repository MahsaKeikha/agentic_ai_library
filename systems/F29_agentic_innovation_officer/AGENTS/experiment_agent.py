class ExperimentAgent:
    name = "experiment_agent"

    def run(self, context):
        return {"agent": self.name, "experiments": context.get("experiments", []), "status": "designed"}
