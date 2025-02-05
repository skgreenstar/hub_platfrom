from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import numpy as np

client = QdrantClient("http://qdrant:6333")
model = SentenceTransformer("all-MiniLM-L6-v2")


def search_documents(query: str):
    query_vector = model.encode([query]).tolist()[0]
    search_result = client.search(collection_name="hub_documents", query_vector=query_vector, limit=3)
    results = [hit.payload["text"] for hit in search_result]
    return {"query": query, "results": results}