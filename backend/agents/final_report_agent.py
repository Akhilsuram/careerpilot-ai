from backend.agents.base_agent import BaseAgent
from backend.orchestrator.agent_metadata import AgentMetadata


class FinalReportAgent(BaseAgent):

    metadata = AgentMetadata(
        name="Final Report Agent",
        version="1.0.0",
        description="Combines outputs from all agents.",
        priority=100,
    )

    def execute(self, context):

        ats = context.outputs.get("ats", {})
        skill_gap = context.outputs.get("skill_gap", {})
        jobs = context.outputs.get("job_match", {})
        roadmap = context.outputs.get("roadmap", {})
        optimizer = context.outputs.get("resume_optimizer", {})
        interview = context.outputs.get("interview", {})

        summary = (
            f"Your ATS score is {ats.get('overall_score', 'N/A')}. "
            f"Resume score is {optimizer.get('resume_score', 'N/A')}. "
            f"You have {len(skill_gap.get('missing_skills', []))} missing skills "
            f"and {len(jobs.get('jobs', []))} recommended job matches."
        )

        strengths = []

        if ats.get("strengths"):
            strengths.extend(ats["strengths"])

        if optimizer.get("recommendations"):
            strengths.extend(
                optimizer["recommendations"][:2]
            )

        weaknesses = []

        if skill_gap.get("missing_skills"):
            weaknesses.extend(skill_gap["missing_skills"])

        next_steps = []

        if roadmap.get("roadmap"):
            for step in roadmap["roadmap"][:5]:
                if isinstance(step, dict):
                    next_steps.append(
                        step.get("title", "")
                    )
                else:
                    next_steps.append(str(step))

        career_advice = (
            "Continue improving your resume, close the identified skill gaps, "
            "practice interview questions regularly, and apply consistently to "
            "roles that closely match your profile."
        )

        return {
            "summary": summary,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "next_steps": next_steps,
            "career_advice": career_advice,
        }