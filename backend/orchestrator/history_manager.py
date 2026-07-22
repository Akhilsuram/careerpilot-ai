import json
from pathlib import Path


class HistoryManager:

    def __init__(self):

        self.file = Path("storage/history.json")

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.file.exists():
            self.file.write_text("[]")

    def save(self, result):

        history = json.loads(
            self.file.read_text()
        )

        history.append(result)

        self.file.write_text(
            json.dumps(history, indent=4)
        )

    def load(self):

        return json.loads(
            self.file.read_text()
        )