from backend.orchestrator.execution_engine import ExecutionEngine


def sample():

    return "CareerPilot AI"


engine = ExecutionEngine()

result = engine.run(
    "sample",
    sample,
)

print(result)