from backend.agents.ats_agent import ATSAgent
from backend.agents.interview_agent import InterviewAgent
from backend.agents.job_match_agent import JobMatchAgent
from backend.agents.resume_optimizer_agent import ResumeOptimizerAgent
from backend.agents.roadmap_agent import RoadmapAgent


class AgentRegistry:

    def __init__(self):

        self._agents = {
            "ats": ATSAgent(),
            "resume_optimizer": ResumeOptimizerAgent(),
            "job_match": JobMatchAgent(),
            "interview": InterviewAgent(),
            "roadmap": RoadmapAgent(),
        }

    def get(
        self,
        name: str,
    ):

        return self._agents.get(name)

    def list_agents(self):

        return list(
            self._agents.keys()
        )
    def metadata(self):

        return {
            key: value.metadata
            for key, value in self._agents.items()
        }