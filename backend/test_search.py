from app.models.database import SessionLocal
from app.services.search_service import semantic_search

db = SessionLocal()

# use document id 1 from the test we did in Step 5
document_id = 1
question = "what is the baggage limit?"

results = semantic_search(db, document_id, question)

print(f"Top {len(results)} chunks for: '{question}'\n")
for r in results:
    print(f"page {r['page_number']} | Score {r['similarity_score']}")
    print(r['chunk_text'])
    print("---")

db.close()