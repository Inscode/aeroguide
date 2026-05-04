from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.services.pdf_service import extract_and_chunk
from app.services.embedding_service import generate_embeddings
from app.services.storage_service import save_document, save_chunks, get_all_documents

router = APIRouter()

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    document_type: str = Form(...),
    db: Session = Depends(get_db),
): 
    file_bytes = await file.read()

    chunks = extract_and_chunk(file_bytes)
    texts = [c["chunk_text"] for c in chunks]
    embeddings = generate_embeddings(texts)

    document = save_document(db, filename=file.filename, document_type=document_type)
    save_chunks(db, document.id, chunks, embeddings)

    return{
        "document_id": document.id,
        "filename": file.filename,
        "document_type": document_type,
        "total_chunks": len(chunks)
    }

@router.get("/")
def list_documents(db: Session = Depends(get_db)):
    documents = get_all_documents(db)
    return [
        {
            "id" : doc.id,
            "filename": doc.filename,
            "document_type": doc.document_type,
            "uploaded_at": doc.uploaded_at
        }
        for doc in documents
    ]
