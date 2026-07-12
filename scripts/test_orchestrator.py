from backend.orchestrator.career_orchestrator import CareerOrchestrator

resume = {
    "name": "SURAM AKHIL",
    "skills": [
        "Python",
        "SQL",
        "FastAPI",
        "Machine Learning",
        "TensorFlow"
    ]
}

goal = "I want an AI Engineer internship in Hyderabad."

orchestrator = CareerOrchestrator()

result = orchestrator.execute(
    resume,
    goal,
)

print(result)