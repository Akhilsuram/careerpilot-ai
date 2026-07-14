from backend.orchestrator.agent_registry import AgentRegistry

registry = AgentRegistry()

for name, metadata in registry.metadata().items():

    print(name)

    print(metadata)