import time

from backend.orchestrator.retry_policy import RetryPolicy


class ExecutionEngine:

    def __init__(self):
        self.retry = RetryPolicy()

    def run(
        self,
        name: str,
        function,
        *args,
        **kwargs,
    ):

        start = time.time()

        try:

            result = self.retry.execute(
                function,
                *args,
                **kwargs,
            )

            elapsed = round(
                time.time() - start,
                2,
            )

            return {
                "success": True,
                "result": result,
                "time": elapsed,
                "error": None,
            }

        except Exception as e:

            elapsed = round(
                time.time() - start,
                2,
            )

            return {
                "success": False,
                "result": None,
                "time": elapsed,
                "error": str(e),
            }