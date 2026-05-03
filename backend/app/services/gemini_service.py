from google import genai
from google.genai import types
import os
import json
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_answer(question: str, chunks: List[Dict]) -> Dict:
    """
    Takes the user question and retrieved chunks,
    builds a prompt, calls Gemini, returns structured answer.
    """
    context = ""
    for i, chunk in enumerate(chunks):
        context += f"\n[Chunk {i+1} | Page {chunk['page_number']}]\n{chunk['chunk_text']}\n"

    prompt = f"""You are an airline document assistant. Answer the user's question using ONLY the context provided below.

Context from document:
{context}

User question: {question}

Instructions:
- Answer only from the provided context. Do not use outside knowledge.
- Use chain-of-thought reasoning to arrive at your answer.
- If the answer is not in the context, say "I could not find this information in the document."
- Respond ONLY with a valid JSON object, no markdown, no backticks, nothing else.

Response format:
{{
  "answer": "your detailed answer here",
  "confidence": "high or medium or low",
  "source_pages": [list of page numbers used],
  "reasoning": "brief explanation of how you arrived at the answer"
}}"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    raw_text = response.text.strip()

    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError:
        parsed = {
            "answer": raw_text,
            "confidence": "low",
            "source_pages": [],
            "reasoning": "Raw response returned, JSON parsing failed."
        }

    return parsed