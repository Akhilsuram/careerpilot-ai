import uuid
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from backend.orchestrator.agent_context import AgentContext
from backend.orchestrator.agent_registry import AgentRegistry
from backend.orchestrator.planner_agent import PlannerAgent
from backend.orchestrator.history_manager import HistoryManager


class CareerCopilot:

    def __init__(self):

        self.registry = AgentRegistry()
        self.planner = PlannerAgent()
        self.history = HistoryManager()

    def run(
        self,
        resume_data: dict,
        target_role: str,
    ):

        context = AgentContext(
            resume_data=resume_data,
            user_goal=target_role,
        )

        # Planner executes first
        self.planner.execute(context)

        agents = {
            "ats": self.registry.get("ats"),
            "job_match": self.registry.get("job_match"),
            "interview": self.registry.get("interview"),
            "roadmap": self.registry.get("roadmap"),
            "skill_gap": self.registry.get("skill_gap"),
            "resume_optimizer": self.registry.get("resume_optimizer"),
            "learning_resources": self.registry.get("learning_resources"),
        }

        def execute_agent(name, agent):

            print(f"[START] {name}")

            context.status[name] = "Running"

            try:
                result = agent.execute(context)

                print(f"[DONE] {name}")

                context.status[name] = "Completed"

                return name, result

            except Exception as e:

                print(f"[FAILED] {name}: {e}")

                context.status[name] = "Failed"

                return name, {
                    "error": str(e)
                }

        with ThreadPoolExecutor(max_workers=4) as executor:

            futures = [
                executor.submit(
                    execute_agent,
                    name,
                    agent,
                )
                for name, agent in agents.items()
            ]

            from concurrent.futures import as_completed

            for future in as_completed(futures):

                name, result = future.result()

                context.outputs[name] = result

        # Final Report (depends on all previous agents)
        report = self.registry.get("final_report")

        context.outputs["final_report"] = report.execute(context)

        # Metadata
        context.outputs["execution"] = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
        }

        context.outputs["agent_status"] = context.status

        # Save history
        # Build result
        result = context.outputs

        # Save history
        self.history.save(result)

        return result