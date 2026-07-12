from backend.services.resume_service import ResumeService


class AnalyzeResumeUseCase:

    def __init__(self, db):

        self.service = ResumeService(db)

    def execute(self, file_path: str):

        return self.service.execute(file_path)
    