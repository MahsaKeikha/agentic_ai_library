from AGENTS.requirements_agent import RequirementsAgent
from AGENTS.hardware_interface_agent import HardwareInterfaceAgent
from AGENTS.firmware_architecture_agent import FirmwareArchitectureAgent
from AGENTS.timing_agent import TimingAgent
from AGENTS.verification_agent import VerificationAgent

class EmbeddedSystemsWorkflow:
    def __init__(self) -> None:
        self.agents = [RequirementsAgent(), HardwareInterfaceAgent(), FirmwareArchitectureAgent(), TimingAgent(), VerificationAgent()]
    def run(self, context: dict) -> list[dict]:
        return [{"agent": a.name, "result": a.run(context)} for a in self.agents]
