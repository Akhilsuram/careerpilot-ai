from backend.orchestrator.retry_policy import RetryPolicy

retry = RetryPolicy(
    retries=2,
    delay=0,
)

count = 0


def sample():

    global count

    count += 1

    if count < 3:

        raise Exception("Retry")

    return "Success"


print(retry.execute(sample))