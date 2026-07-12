from backend.agents.ats_agent import ATSAgent

resume = {
    "skills": [
        "Python",
        "SQL",
        "FastAPI",
        "Machine Learning"
    ]
}

jd = """
We are looking for a Data Scientist.

Required:

Python

SQL

Docker

AWS

FastAPI

Machine Learning
"""

agent = ATSAgent()

response = agent.analyze(
    resume,
    jd
)

print(response)