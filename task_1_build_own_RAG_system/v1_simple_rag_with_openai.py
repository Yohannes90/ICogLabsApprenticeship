import os
from openai import OpenAI
from dotenv import load_dotenv


# Configuration
load_dotenv()
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Jaccard similarity function
def jaccard_similarity(query, document):
    query = query.lower().split()
    document = document.lower().split()
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union) if union else 0

# Find the most relevant document
def return_response(query, corpus):
    similarities = [jaccard_similarity(query, doc) for doc in corpus]
    return corpus[similarities.index(max(similarities))]

# Corpus of documents
corpus_of_documents = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters."
]

# Get user input
user_input = input("What activity would you like to do today? ")

# Find relevant document
relevant_document = return_response(user_input, corpus_of_documents)

# Generate prompt
prompt = f"""
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
"""

# Generate response using OpenAI API
response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

# Print the response
print(response.choices[0].message.content)
