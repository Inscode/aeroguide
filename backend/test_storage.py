from app.models.database import SessionLocal, create_tables
from app.services.storage_service import save_document, save_chunks, get_all_documents
from app.services.embedding_service import generate_embeddings

create_tables()
db = SessionLocal()

# fake chunks
chunks = [
    {"chunk_index": 0, "page_number": 1, "chunk_text": "Passengers must check in 2 hours before departure."},
    {"chunk_index": 1, "page_number": 2, "chunk_text": "Carry-on baggage must not exceed 7kg."}, 
]

#generate all embeddings
texts = [c["chunk_text"] for c in chunks] 
embeddings = generate_embeddings(texts)

# save to db
document = save_document(db, filename="test_policy.pdf", document_type="passenger_policy")
print(f"Document saved with id: {document.id}")

save_chunks(db, document.id, chunks, embeddings)
print("chunks saved successfully ")

#verify
all_docs = get_all_documents(db)
print(f"Total documents in DB: {len(all_docs)}")

db.close()