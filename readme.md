# AeroGuide — Airline Knowledge Intelligence System

A RAG-powered assistant that answers natural language questions from uploaded airline documents (passenger policies, flight regulations, airport procedures, operational manuals), returning accurate answers with page citations.

## Tech Stack

- **Backend** — FastAPI, Python 3.12
- **Embeddings** — Hugging Face sentence-transformers (all-MiniLM-L6-v2)
- **Vector Store** — pgvector on PostgreSQL
- **LLM** — Google Gemini API
- **Frontend** — React.js
- **Deployment** — AWS EC2, Docker, GitHub Actions

## Status

🚧 Under active development

## Architecture

```
PDF Upload → Text Extraction → Chunking → Embedding → pgvector Storage
                                                              ↓
User Question → Embed Question → Cosine Similarity Search → Top 5 Chunks
                                                              ↓
                                              Gemini API → Answer + Citations
```

## Running Locally

Documentation coming after initial release.