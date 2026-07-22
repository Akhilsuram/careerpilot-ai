import time

from backend.agents.resume_agent import ResumeAgent
from backend.models.resume import Resume, ResumeStatus
from backend.repositories.resume_repository import ResumeRepository
from backend.tools.pdf_parser import PDFParser
from backend.utils.response_builder import ResponseBuilder


class ResumeService:

    def __init__(self, db):
        self.repository = ResumeRepository(db)
        self.agent = ResumeAgent()

    def execute(self, file_path: str):

        start = time.time()

        PDFParser.validate(file_path)
        print("STEP 1 - PDF validated")

        text = PDFParser.extract_text(file_path)
        print("STEP 2 - Text extracted")
        print("\n========== EXTRACTED TEXT ==========")
        print(text[:3000])
        print("====================================")

        content_hash = PDFParser.generate_hash(file_path)
        print("STEP 3 - Hash generated")

        # Check if resume already exists
        existing_resume = self.repository.get_by_hash(content_hash)
        print("STEP 4 - Checking existing resume")

        if existing_resume:

            processing_time = 0

            result = {
                "resume": existing_resume,
                "text": existing_resume.extracted_text,
                "hash": existing_resume.content_hash,
                "parsed": existing_resume.parsed_json,
            }

            return ResponseBuilder.success(
                message="Resume already analyzed.",
                data=result,
                processing_time=processing_time,
            )

        # Analyze Resume
        try:
            parsed = self.agent.analyze(text)
            print("STEP 5 - Calling ResumeAgent")
            print(">>> ResumeAgent.analyze() completed")
            print(">>> Calling ResumeAgent.analyze()")
            print("STEP 6 - ResumeAgent completed")

        except Exception as e:

            return ResponseBuilder.error(
                message=f"Resume analysis failed: {str(e)}"
            )

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
        print("STEP 7 - Saving to database")
        

        processing_time = round(time.time() - start, 2)
        print("STEP 8 - Finished")

        result = {
            "resume": resume,
            "text": text,
            "hash": content_hash,
            "parsed": parsed,
        }

        return ResponseBuilder.success(
            message="Resume analyzed successfully.",
            data=result,
            processing_time=processing_time,
        )