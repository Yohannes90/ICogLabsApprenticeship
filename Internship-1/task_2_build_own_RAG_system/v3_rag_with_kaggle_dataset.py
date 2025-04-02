import pandas as pd
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
from chromadb import Client
from chromadb.config import Settings

# Load and clean dataset
def load_and_clean_dataset(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['Title', 'Description'])  # Drop rows with missing fields
    return df.head(3)

# Apply chat template
def apply_chat_template(title, description):
    system_message = "You are a helpful assistant summarizing machine learning research papers."
    user_message = f"The paper titled '{title}' has the following description:\n{description}\nSummarize this paper in two concise sentences."
    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]

# Initialize Hugging Face model and tokenizer
def initialize_hf_model(model_name="EleutherAI/gpt-neo-2.7B"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

# Generate response from chat model
def generate_response(messages, tokenizer, model):
    # Flatten chat template into a single input string
    input_text = "\n".join([msg["content"] for msg in messages])
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

# Store embeddings and outputs in ChromaDB
def store_in_chromadb(collection_name, docs, embeddings):
    client = Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./chromadb"
    ))
    collection = client.get_or_create_collection(name=collection_name)
    collection.add(
        documents=[doc['description'] for doc in docs],
        metadatas=[{"title": doc['title'], "output": doc['output']} for doc in docs],
        ids=[str(i) for i in range(len(docs))],
        embeddings=embeddings
    )

# Main function
def main():
    # Load and clean dataset
    file_path = "ml-potw-10232023.csv"
    df = load_and_clean_dataset(file_path)

    # Initialize SentenceTransformer and Hugging Face model
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    tokenizer, model = initialize_hf_model()

    # Process dataset
    processed_data = []
    embeddings = []
    for _, row in df.iterrows():
        title, description = row['Title'], row['Description']
        # Apply chat template and generate response
        messages = apply_chat_template(title, description)
        output = generate_response(messages, tokenizer, model)

        # Generate embedding for the description
        embedding = embedder.encode(description)

        # Append results
        processed_data.append({"title": title, "description": description, "output": output})
        embeddings.append(embedding)

    # Store in ChromaDB
    store_in_chromadb("ml_papers_collection", processed_data, embeddings)

if __name__ == "__main__":
    main()
