from AGENTS.schema_agent import SchemaAgent
from AGENTS.query_performance_agent import QueryPerformanceAgent
from AGENTS.migration_agent import MigrationAgent
from AGENTS.resilience_agent import ResilienceAgent
from AGENTS.security_agent import SecurityAgent

class DatabaseArchitectureWorkflow:
    def __init__(self) -> None:
        self.agents = [SchemaAgent(), QueryPerformanceAgent(), MigrationAgent(), ResilienceAgent(), SecurityAgent()]
    def run(self, context: dict) -> list[dict]:
        return [{"agent": a.name, "result": a.run(context)} for a in self.agents]
