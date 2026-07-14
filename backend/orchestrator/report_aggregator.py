class ReportAggregator:

    def aggregate(
        self,
        context,
    ):

        return {

    "plan": context.planner_output,

    "results": context.results,

    "execution_log": context.execution_log,

    "execution_trace": [

        trace.__dict__

        for trace in context.trace

    ],

    "timings": context.timings,

    "completed_agents": list(context.results.keys()),

    "successful_agents": len(context.results),

}