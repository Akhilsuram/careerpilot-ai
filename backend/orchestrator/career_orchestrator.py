from backend.agents.ats_agent import ATSAgent
from backend.agents.interview_agent import InterviewAgent
from backend.agents.job_match_agent import JobMatchAgent
from backend.agents.planner_agent import PlannerAgent
from backend.agents.resume_optimizer_agent import ResumeOptimizerAgent
from backend.agents.roadmap_agent import RoadmapAgent
from backend.orchestrator.agent_registry import AgentRegistry
from backend.orchestrator.execution_context import ExecutionContext
from backend.orchestrator.execution_engine import ExecutionEngine
from backend.orchestrator.report_aggregator import ReportAggregator
from backend.orchestrator.task_scheduler import TaskScheduler


class CareerOrchestrator:

    def __init__(self):

        self.planner = PlannerAgent()

        self.scheduler = TaskScheduler()

        self.engine = ExecutionEngine()

        self.aggregator = ReportAggregator()

        self.registry = AgentRegistry()

    def execute(
        self,
        resume_data: dict,
        user_goal: str,
    ):

        context = ExecutionContext(
            resume_data=resume_data,
            user_goal=user_goal,
        )

        context.planner_output = self.planner.plan(
            user_goal
        )

        role = context.planner_output.get(
            "target_role",
            "",
        )

        location = context.planner_output.get(
            "location",
            "",
        )

        schedule = self.scheduler.build_schedule(
            context.planner_output
        )

        for agent_name in schedule:

            if agent_name == "ats":

                result = self.engine.run(
                    "ats",
                    self.registry.get("ats").analyze,
                    resume_data,
                    user_goal,
                )

            elif agent_name == "resume_optimizer":

                result = self.engine.run(
                    "resume_optimizer",
                    self.registry.get("resume_optimizer").optimize,
                    resume_data,
                    role,
                )

            elif agent_name == "job_match":

                result = self.engine.run(
                    "job_match",
                    self.registry.get("job_match").find_jobs,
                    resume_data,
                    role,
                    location,
                )

            elif agent_name == "interview":

                result = self.engine.run(
                    "interview",
                    self.registry.get("interview").generate_questions,
                    resume_data,
                    role,
                    user_goal,
                )

            elif agent_name == "roadmap":

                result = self.engine.run(
                    "roadmap",
                    self.registry.get("roadmap").generate,
                    resume_data,
                    role,
                )

            else:
                continue

            context.execution_log.append(
                {
                    "agent": agent_name,
                    "status": result["success"],
                }
            )

            context.timings[agent_name] = result["time"]

            if result["success"]:

                context.results[agent_name] = result["result"]

        return self.aggregator.build(
            context
        )