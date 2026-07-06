from pydantic import BaseModel


class GenerateExamRequest(BaseModel):
    subject: str
    topic: str
    difficulty: str
    number_of_questions: int