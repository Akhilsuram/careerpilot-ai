from backend.orchestrator.agent_registry import AgentRegistry

registry = AgentRegistry()

print(registry.list_agents())

print(type(registry.get("ats")).__name__)

print(type(registry.get("job_match")).__name__)