from fastapi import APIRouter

from app.rag.service import RAGService
from app.schemas.requests import GenerateExamRequest

router = APIRouter()

rag = RAGService()


@router.post("/test")
def generate_test(request: GenerateExamRequest):

    exam = rag.generate_exam(
        subject=request.subject,
        topic=request.topic,
        difficulty=request.difficulty,
        number_of_questions=request.number_of_questions,
    )

    return {
        "exam": exam
    }