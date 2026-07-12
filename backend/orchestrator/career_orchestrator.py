from backend.agents.ats_agent import ATSAgent
from backend.agents.interview_agent import InterviewAgent
from backend.agents.job_match_agent import JobMatchAgent
from backend.agents.planner_agent import PlannerAgent
from backend.agents.resume_optimizer_agent import ResumeOptimizerAgent
from backend.agents.roadmap_agent import RoadmapAgent


class CareerOrchestrator:

    def __init__(self):

        self.planner = PlannerAgent()

        self.ats = ATSAgent()

        self.optimizer = ResumeOptimizerAgent()

        self.jobs = JobMatchAgent()

        self.interview = InterviewAgent()

        self.roadmap = RoadmapAgent()

    def execute(
        self,
        resume_data: dict,
        user_goal: str,
    ):

        plan = self.planner.plan(user_goal)

        report = {
            "plan": plan
        }

        role = plan.get("target_role", "")

        location = plan.get("location", "")

        agents = plan.get("agents", [])

        if "ats" in agents:

            report["ats"] = self.ats.analyze(
                resume_data,
                user_goal,
            )

        if "resume_optimizer" in agents:

            report["resume_optimizer"] = self.optimizer.optimize(
                resume_data,
                role,
            )

        if "job_match" in agents:

            report["job_matches"] = self.jobs.find_jobs(
                resume_data,
                role,
                location,
            )

        if "interview" in agents:

            report["interview"] = self.interview.generate_questions(
                resume_data,
                role,
                user_goal,
            )

        if "roadmap" in agents:

            report["roadmap"] = self.roadmap.generate(
                resume_data,
                role,
            )

        return report