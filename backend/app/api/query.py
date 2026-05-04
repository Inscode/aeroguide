from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.models.database import get_db
from app.services.search_service import semantic_search
from app.services.gemini_service import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    document_id: int
    question: str

@router.post("/ask")
def ask_question(request: QueryRequest, db: Session = Depends(get_db)):
    chunks = semantic_search(db, request.document_id, request.question)
    answer = generate_answer(request.question, chunks)

    return {
        "question": request.question,
        "document_id": request.document_id,
        "answer": answer.get("answer"),
        "confidence": answer.get("confidence"),
        "source_pages": answer.get("source_pages"),
        "reasoning": answer.get("reasoning")
    }