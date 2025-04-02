import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chromadb.config import Settings
from chromadb import Client
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from openai import OpenAI
from google.colab import userdata

# Initialize FastAPI
app = FastAPI()

# Setup GitHub Marketplace OpenAI client
GITHUB_TOKEN = userdata.get('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN not found. Please set it in your environment.")
OPENAI_ENDPOINT = "https://models.inference.ai.azure.com"
MODEL_NAME = "gpt-4o-mini"

openai_client = OpenAI(base_url=OPENAI_ENDPOINT, api_key=GITHUB_TOKEN)

# Setup ChromaDB
chroma_client = Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./chroma_data"  # Directory to store the database
    )
)
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Initialize collection
collection_name = "documents"
if collection_name not in chroma_client.list_collections():
    collection = chroma_client.create_collection(collection_name, embedding_function)
else:
    collection = chroma_client.get_collection(collection_name)

# Load a dataset (e.g., small set of FAQs or text samples)
@app.on_event("startup")
def load_dataset():
    documents = [
        {"id": "1", "text": "What is RAG?"},
        {"id": "2", "text": "Explain how vector databases work."},
        {"id": "3", "text": "How does GPT-4 generate text?"}
    ]
    for doc in documents:
        collection.add(
            documents=[doc["text"]],
            metadatas=[{"source": "FAQ"}],
            ids=[doc["id"]]
        )
    print("Dataset loaded into ChromaDB.")

# Request model
class Query(BaseModel):
    user_query: str

@app.post("/query")
async def query_rag(query: Query):
    # Step 1: Embed the query
    query_embedding = embedding_function(query.user_query)

    # Step 2: Retrieve top-k relevant documents
    results = collection.query(query_embeddings=[query_embedding], n_results=3)

    if not results["documents"]:
        raise HTTPException(status_code=404, detail="No relevant documents found.")

    # Step 3: Use OpenAI model to generate a response
    context = " ".join(results["documents"][0])
    prompt = f"Context: {context}\n\nQuestion: {query.user_query}\n\nAnswer:"
    response = openai_client.completions.create(
        model=MODEL_NAME,
        prompt=prompt,
        max_tokens=150
    )

    return {"response": response.choices[0].text.strip()}
