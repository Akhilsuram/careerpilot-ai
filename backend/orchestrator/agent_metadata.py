from dataclasses import dataclass


@dataclass
class AgentMetadata:

    name: str

    version: str

    description: str

    priority: int

    enabled: bool = True