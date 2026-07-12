from backend.agents.roadmap_agent import RoadmapAgent

resume = {
    "skills": [
        "Python",
        "SQL",
        "Machine Learning"
    ]
}

agent = RoadmapAgent()

result = agent.generate(
    resume,
    "AI Engineer",
)

print(result)