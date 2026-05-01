from app.services.pdf_service import extract_and_chunk


# use any small pdf 

with open("test.pdf", "rb") as f:
    file_bytes = f.read()

chunks = extract_and_chunk(file_bytes)

print(f"Total chunks: {len(chunks)}")

for chunk in chunks[:3]:
    print(f"\n---Chunk {chunk['chunk_index']} | Page {chunk['page_number']} ---")
    print(chunk['chunk_text'])
