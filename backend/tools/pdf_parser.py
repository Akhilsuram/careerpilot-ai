import hashlib
from pathlib import Path

import fitz

from backend.core.exceptions import ResumeParsingException


class PDFParser:

    @staticmethod
    def extract_text(file_path: str) -> str:
        try:

            document = fitz.open(file_path)

            text = ""

            for page in document:
                text += page.get_text()

            document.close()

            return text.strip()

        except Exception as e:
            raise ResumeParsingException(str(e))

    @staticmethod
    def generate_hash(file_path: str) -> str:

        sha = hashlib.sha256()

        with open(file_path, "rb") as file:

            while chunk := file.read(8192):
                sha.update(chunk)

        return sha.hexdigest()

    @staticmethod
    def validate(file_path: str):

        path = Path(file_path)

        if not path.exists():
            raise ResumeParsingException("Resume not found.")

        if path.suffix.lower() != ".pdf":
            raise ResumeParsingException("Only PDF files are supported.")

        return True