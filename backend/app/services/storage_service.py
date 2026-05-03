from sqlalchemy.orm import Session
from app.models.database import Document, DocumentChunk
from typing import List, Dict


def save_document(db: Session, filename: str, document_type: str) -> Document: 
    """
    Create a document record in the documents table and returns it.
    """

    document = Document(filename=filename, document_type=document_type)
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


def save_chunks(db: Session, document_id: int, chunks: List[Dict], embeddings: List[List[float]]) -> None: 
    """
    Takes document id, list of chunks , and their embeddings,
    inserts each chunk with tis embedding into document_chunks table.
    """

    for chunk, embedding in zip(chunks, embeddings):
        doc_chunk = DocumentChunk(
            document_id=document_id,
            chunk_text=chunk["chunk_text"],
            chunk_index=chunk["chunk_index"],
            page_number=chunk["page_number"],
            embedding=embedding
        )
        db.add(doc_chunk)
    db.commit()

def get_all_documents(db: Session) -> list[Document]:
    """
    Returns all upload documents.
    """
    return db.query(Document).order_by(Document.uploaded_at.desc()).all()