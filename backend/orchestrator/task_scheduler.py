class TaskScheduler:

    AGENT_ORDER = [
        "ats",
        "resume_optimizer",
        "job_match",
        "interview",
        "roadmap",
    ]

    def build_schedule(
        self,
        planner_output: dict,
    ):

        selected = planner_output.get(
            "agents",
            [],
        )

        schedule = []

        for agent in self.AGENT_ORDER:

            if agent in selected:

                schedule.append(agent)

        return schedule