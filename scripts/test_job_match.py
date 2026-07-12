from backend.agents.job_match_agent import JobMatchAgent

resume = {
    "skills": [
        "Python",
        "SQL",
        "FastAPI",
        "Machine Learning",
        "TensorFlow",
    ]
}

agent = JobMatchAgent()

response = agent.find_jobs(
    resume,
    "AI Engineer",
    "Hyderabad",
)

print(response)