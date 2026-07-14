from dataclasses import dataclass, field


@dataclass
class ExecutionContext:

    resume_data: dict

    user_goal: str

    planner_output: dict = field(default_factory=dict)

    results: dict = field(default_factory=dict)

    execution_log: list = field(default_factory=list)

    timings: dict = field(default_factory=dict)

    trace: list = field(default_factory=list)