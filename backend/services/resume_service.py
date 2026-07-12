import time

from backend.agents.resume_agent import ResumeAgent
from backend.repositories.resume_repository import ResumeRepository
from backend.tools.pdf_parser import PDFParser


class ResumeService:

    def __init__(self, db):

        self.repository = ResumeRepository(db)

        self.agent = ResumeAgent()

    def execute(self, file_path: str):

        start = time.time()

        PDFParser.validate(file_path)

        text = PDFParser.extract_text(file_path)

        content_hash = PDFParser.generate_hash(file_path)

        parsed = self.agent.analyze(text)

        elapsed = round(time.time() - start, 2)

        return {
            "text": text,
            "hash": content_hash,
            "parsed": parsed,
            "processing_time": elapsed,
        }