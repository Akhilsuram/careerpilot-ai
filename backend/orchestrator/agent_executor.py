class AgentExecutor:

    def execute(
        self,
        agent,
        context,
    ):

        return agent.execute(context)