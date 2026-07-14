from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExecutionTrace:

    agent: str

    provider: str

    status: bool

    execution_time: float

    retries: int

    timestamp: str = datetime.utcnow().isoformat()