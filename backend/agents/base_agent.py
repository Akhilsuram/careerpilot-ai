from abc import ABC

from backend.orchestrator.agent_metadata import AgentMetadata


class BaseAgent(ABC):

    metadata: AgentMetadata

    def execute(
        self,
        context,
    ):
        raise NotImplementedError