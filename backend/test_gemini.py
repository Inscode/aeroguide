from app.models.database import SessionLocal
from app.services.search_service import semantic_search
from app.services.gemini_service import generate_answer

db = SessionLocal()

document_id = 1
question = "What is the buggage limit?"

chunks = semantic_search(db, document_id, question)
answer = generate_answer(question, chunks)


print(f"Question: {question}\n")
print(f"Answer: {answer['answer']}")
print(f"confidence: {answer['confidence']}")
print(f"Source Pages: {answer['source_pages']}")
print(f"Reasoning: {answer['reasoning']}")


db.close()
