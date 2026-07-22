from pydantic import BaseModel


class CareerCopilotRequest(BaseModel):

    resume_data: dict
    target_role: str