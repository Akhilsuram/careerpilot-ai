from datetime import datetime


class ExecutionLogger:

    def log(
        self,
        agent: str,
        success: bool,
        elapsed: float,
    ):

        return {
            "agent": agent,
            "status": success,
            "time": elapsed,
            "timestamp": datetime.utcnow().isoformat(),
        }