import time


class RetryPolicy:

    def __init__(
        self,
        retries: int = 2,
        delay: float = 1,
    ):

        self.retries = retries
        self.delay = delay

    def execute(
        self,
        function,
        *args,
        **kwargs,
    ):

        last_exception = None

        for _ in range(self.retries + 1):

            try:

                return function(
                    *args,
                    **kwargs,
                )

            except Exception as e:

                last_exception = e

                time.sleep(self.delay)

        raise last_exception