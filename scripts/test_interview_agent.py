from backend.agents.interview_agent import InterviewAgent

resume = {
    "name": "SURAM AKHIL",
    "skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "FastAPI",
    ],
}

agent = InterviewAgent()

response = agent.generate_questions(
    resume,
    "AI Engineer",
)

print(response)