class ReportAggregator:

    def aggregate(
        self,
        context,
    ):

        return {
            "plan": context.planner_output,
            "ats": context.results.get("ats"),
            "resume_optimizer": context.results.get("resume_optimizer"),
            "job_matches": context.results.get("job_match"),
            "interview": context.results.get("interview"),
            "roadmap": context.results.get("roadmap"),
            "execution_log": context.execution_log,
            "timings": context.timings,
            "completed_agents": list(
                context.results.keys()
            ),
            "successful_agents": len(
                context.results
            ),
        }