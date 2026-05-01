import fitz
from typing import List, Dict

def extract_and_chunk(file_bytes: bytes, chunk_size: int = 500, overlap: int = 50) -> List[Dict]:

    """
    Accetps PDF as bytes, extracts text page by page,
    splits into overlapping chunks, returns list of chunk dicts.
    """

    doc = fitz.open(stream=file_bytes, filetype="pdf")

    all_chunks = []
    chunk_index = 0

    for page_num in range(len(doc)):
        page = doc[page_num]
        page_text = page.get_text()

        if not page_text.strip():
            continue
        
        words = page_text.split()

        #  slide window of chunk size words with overlap
        start = 0
        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]
            chunk_text = " ".join(chunk_words)

            all_chunks.append({
                "chunk_index": chunk_index,
                "page_number": page_num + 1,
                "chunk_text": chunk_text
            })

            chunk_index += 1
            start += chunk_size - overlap

    doc.close()
    return all_chunks