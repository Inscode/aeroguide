from sqlalchemy.orm import Session
from app.models.database import DocumentChunk
from app.services.embedding_service import generate_single_embedding
from typing import List, Dict

def semantic_search(db:Session, document_id: int, question: str, top_k: int=5) -> List[Dict]:
    """
    Embeds the user question, queries pgvector for the top_k most similar
    chunks from the given document using cosine similarity.
    """

    question_embedding = generate_single_embedding(question)

    results = (
        db.query(
            DocumentChunk, DocumentChunk.embedding.cosine_distance(question_embedding).label("distance")
        )
        .filter(DocumentChunk.document_id == document_id)
        .order_by("distance")
        .limit(top_k)
        .all()
    )

    chunks = []
    for chunk, distance in results:
        chunks.append( {
            "chunk_text": chunk.chunk_text,
            "page_number": chunk.page_number,
            "chunk_index": chunk.chunk_index,
            "similarity_score": round(1 - distance, 4) # convert distance to similarity        
            })
        
        return chunks