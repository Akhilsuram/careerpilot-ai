import time

from backend.agents.resume_agent import ResumeAgent
from backend.models.resume import Resume, ResumeStatus
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

        # Check if resume already exists
        existing_resume = self.repository.get_by_hash(content_hash)

        if existing_resume:

            return {
                "resume": existing_resume,
                "text": existing_resume.extracted_text,
                "hash": existing_resume.content_hash,
                "parsed": existing_resume.parsed_json,
                "processing_time": 0,
            }

        # Analyze Resume
        parsed = self.agent.analyze(text)

        # Create Resume object
        resume = Resume(
            filename=file_path.split("/")[-1].split("\\")[-1],
            original_filename=file_path.split("/")[-1].split("\\")[-1],
            file_path=file_path,
            content_hash=content_hash,
            extracted_text=text,
            parsed_json=parsed,
            status=ResumeStatus.PARSED,
        )

        # Save to database
        resume = self.repository.create(resume)

        elapsed = round(time.time() - start, 2)

        return {
            "resume": resume,
            "text": text,
            "hash": content_hash,
            "parsed": parsed,
            "processing_time": elapsed,
        }