from AGENTS.device_onboarding_agent import DeviceOnboardingAgent
from AGENTS.telemetry_agent import TelemetryAgent
from AGENTS.edge_processing_agent import EdgeProcessingAgent
from AGENTS.connectivity_agent import ConnectivityAgent
from AGENTS.fleet_operations_agent import FleetOperationsAgent

class IoTEngineeringWorkflow:
    def __init__(self) -> None:
        self.agents = [DeviceOnboardingAgent(), TelemetryAgent(), EdgeProcessingAgent(), ConnectivityAgent(), FleetOperationsAgent()]
    def run(self, context: dict) -> list[dict]:
        return [{"agent": a.name, "result": a.run(context)} for a in self.agents]
