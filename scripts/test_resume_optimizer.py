from backend.agents.resume_optimizer_agent import ResumeOptimizerAgent

resume = {
    "summary": "Python developer.",
    "skills": [
        "Python",
        "SQL"
    ],
    "projects": [
        {
            "name": "CareerPilot AI"
        }
    ],
    "experience": []
}

agent = ResumeOptimizerAgent()

response = agent.optimize(
    resume,
    "AI Engineer"
)

print(response)