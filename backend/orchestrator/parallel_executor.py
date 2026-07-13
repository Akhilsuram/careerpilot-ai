from concurrent.futures import ThreadPoolExecutor, as_completed


class ParallelExecutor:

    def run(
        self,
        tasks: list,
    ):

        results = {}

        with ThreadPoolExecutor(
    max_workers=min(
        len(tasks),
        5,
    )
) as executor:

            futures = {
                executor.submit(task["function"]): task["name"]
                for task in tasks
            }

            for future in as_completed(futures):

                name = futures[future]

                try:

                    results[name] = future.result()

                except Exception as e:

                    results[name] = {
                        "success": False,
                        "error": str(e),
                    }

        return results