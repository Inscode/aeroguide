
from app.services.embedding_service import generate_embeddings, generate_single_embedding

texts = [
    "Passengers must check in at least 2 hours before departure.",
    "carry-on baggage must not exceed 7kg."
]

embeddings = generate_embeddings(texts)

print(f"Number of embeddings: {len(embeddings)}")
print(f"Dimension of each embedding: {len(embeddings[0])}")
print(f"First 5 values of embedding 1: {embeddings[0][:5]}")

question_embedding = generate_single_embedding("What is the baggage limit?")
print(f"\nQuestion embedding dimension: {len(question_embedding)}")