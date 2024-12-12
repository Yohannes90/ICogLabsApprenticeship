# Import required libraries
import os
from openai import OpenAI
import chromadb
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Initialize OpenAI client
print("\n\n\n\nInitializing OpenAI client...")
token = os.environ["GITHUB"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Define the corpus of documents
print("\n\n\nDefining corpus of documents...")
corpus_of_documents = [
    "Take a leisurely walk in the park, enjoy the fresh air, and relax under a shaded tree while reading your favorite book.",
    "Visit a local museum to explore historical artifacts, learn about cultural heritage, and gain a deeper understanding of the region.",
    "Attend a live music concert to experience the thrill of live performances and connect with fellow music enthusiasts.",
    "Go for a hike in the mountains, breathe in the fresh air, admire the panoramic views, and discover hidden waterfalls.",
    "Have a picnic with friends at a scenic spot, share homemade dishes, and create lasting memories with laughter and fun.",
    "Explore a new cuisine by visiting an authentic ethnic restaurant, tasting unique dishes, and learning about its cultural significance.",
    "Join a yoga class to improve flexibility, focus on mindfulness, and enjoy the calming atmosphere of a wellness center.",
    "Participate in a local sports league to stay active, build camaraderie, and challenge yourself in a friendly competitive environment.",
    "Attend an educational workshop on photography techniques and capture stunning pictures of your surroundings.",
    "Visit an amusement park for a day filled with thrilling roller coasters, family-friendly attractions, and delightful treats.",
    "Take a pottery class and create handmade pieces while learning a new skill that combines creativity and relaxation.",
    "Volunteer at a community event to give back, meet new people, and contribute positively to a meaningful cause.",
    "Book a weekend getaway to a nearby city, explore its landmarks, try local dishes, and unwind from your routine.",
    "Go stargazing at night in a quiet location, learn about constellations, and enjoy the peaceful beauty of the starry sky.",
    "Take a cooking class to learn how to prepare delicious meals, enhance your culinary skills, and enjoy your creations.",
    "Visit a botanical garden to admire the variety of plants, enjoy the vibrant colors, and learn about biodiversity."
]

# Initialize ChromaDB client and index the corpus
print("\n\nInitializing ChromaDB client and indexing corpus...")
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="indexed_corpus_of_documents")

collection.add(
    documents=corpus_of_documents,
    metadatas=[{"source": str(i)} for i in range(len(corpus_of_documents))],
    ids=[str(i) for i in range(len(corpus_of_documents))]
)

# Query the collection
query_text = "I like long walks and traveling, I recently went to Hawaii."
print(f"\n\nQuerying the collection with: {query_text}")
results = collection.query(query_texts=[query_text], n_results=2)
print(f"Query results: {results}")

# Initialize sentence transformer model
print("Initializing sentence transformer model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(query, corpus):
    print(f"\n\nComputing similarity for query: '{query}'")
    query_embedding = model.encode([query])
    doc_embeddings = model.encode(corpus)
    similarities = cosine_similarity(query_embedding, doc_embeddings)
    print(f"Similarity scores computed.")
    return similarities


def ranking_documents(similarities):
    print("\n\nRanking documents based on similarity scores...")
    indexed = list(enumerate(similarities[0]))
    sorted_index = sorted(indexed, key=lambda x: x[1], reverse=True)
    print("Documents ranked successfully.")
    return sorted_index


def recommended_documents(sorted_index, corpus_of_documents):
    print("\n\nSelecting recommended documents...")
    recommended_docs = []
    for value, score in sorted_index:
        if score > 0.3:
            formatted_score = "{:.2f}".format(score)

            print(f"{formatted_score} => {corpus_of_documents[value]}")
            recommended_docs.append(corpus_of_documents[value])

    print("Recommendations selected.")
    return recommended_docs


def generate_llm_response(prompt):
    print("\n\n\n\nGenerating response from language model...")
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a bot that makes recommendations for activities."},
            {"role": "user", "content": prompt}
        ],
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model_name
    )
    print("Response generated successfully.")
    return response.choices[0].message.content


# User interaction and recommendation process
user_input = input("What activity would you like to do today? ")

print(f"User input: {user_input}")

similarities = compute_similarity(user_input, corpus_of_documents)
ranked_documents = ranking_documents(similarities)
recommended_docs = recommended_documents(ranked_documents, corpus_of_documents)

print(f"\n\nRecommended activities: {recommended_docs}")

prompt = f"""
You are a bot that makes recommendations for activities. You answer in very clear recommendation.
These is a list of potential activities:
{recommended_docs}
The user's query is: {user_input}
Provide the user with 2 recommended activities based on potential activities.
"""

final_recommendation = generate_llm_response(prompt)

print("\n\nFinal Recommendation:")

print(f"{final_recommendation}")
