from dataclasses import dataclass, field



@dataclass
class AgentContext:

    resume_data: dict

    user_goal: str

    planner_output: dict = field(default_factory=dict)

    outputs: dict = field(default_factory=dict)

    status: dict = field(default_factory=dict)