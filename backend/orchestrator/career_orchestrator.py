from backend.agents.planner_agent import PlannerAgent
from backend.orchestrator.agent_registry import AgentRegistry
from backend.orchestrator.agent_executor import AgentExecutor
from backend.orchestrator.execution_context import ExecutionContext
from backend.orchestrator.execution_engine import ExecutionEngine
from backend.orchestrator.execution_logger import ExecutionLogger
from backend.orchestrator.parallel_executor import ParallelExecutor
from backend.orchestrator.report_aggregator import ReportAggregator
from backend.orchestrator.task_scheduler import TaskScheduler


class CareerOrchestrator:

    def __init__(self):

        self.planner = PlannerAgent()

        self.parallel = ParallelExecutor()

        self.logger = ExecutionLogger()

        self.scheduler = TaskScheduler()

        self.engine = ExecutionEngine()

        self.aggregator = ReportAggregator()

        self.registry = AgentRegistry()

        self.executor = AgentExecutor()

    def execute(
        self,
        resume_data: dict,
        user_goal: str,
    ):

        context = ExecutionContext(
            resume_data=resume_data,
            user_goal=user_goal,
        )

        # Planner
        context.planner_output = self.planner.plan(user_goal)

        schedule = self.scheduler.build_schedule(
            context.planner_output
        )

        tasks = []

        for agent_name in schedule:

            agent = self.registry.get(agent_name)

            tasks.append(
                {
                    "name": agent_name,
                    "function": lambda a=agent, n=agent_name: self.engine.run(
                        n,
                        self.executor.execute,
                        a,
                        context,
                    ),
                }
            )

        # Run agents
        results = self.parallel.run(tasks)

        for agent_name, result in results.items():

            context.execution_log.append(
                self.logger.log(
                    agent_name,
                    result["success"],
                    result.get("time", 0),
                )
            )

            context.timings[agent_name] = result.get(
                "time",
                0,
            )

            if result["success"]:

                context.results[agent_name] = result["result"]

        # Aggregate final report
        report = self.aggregator.aggregate(context)

        return report