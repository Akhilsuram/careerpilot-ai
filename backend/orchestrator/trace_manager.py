from backend.orchestrator.execution_trace import ExecutionTrace


class TraceManager:

    def create(
        self,
        agent,
        provider,
        success,
        execution_time,
        retries,
    ):

        return ExecutionTrace(
            agent=agent,
            provider=provider,
            status=success,
            execution_time=execution_time,
            retries=retries,
        )