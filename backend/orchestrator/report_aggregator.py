class ReportAggregator:

    def build(
        self,
        context,
    ):

        return {
            "plan": context.planner_output,
            "results": context.results,
            "execution_log": context.execution_log,
            "timings": context.timings,
            "completed_agents": list(
                context.results.keys()
            ),
            "successful_agents": len(
                context.results
            ),
        }