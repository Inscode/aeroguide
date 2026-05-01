from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np


# load model only at startup - not every request
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Takes a list of text strings, returens a list of 384-dimension vectors.
    """

    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings.tolist()

def generate_single_embedding(text: str) -> List[float]:
    """
    Takes a single text string, returns one 384-dimension vector. used for embedding
    the user's question at query time.
    """

    embedding = model.encode([text])
    return embedding[0].tolist()