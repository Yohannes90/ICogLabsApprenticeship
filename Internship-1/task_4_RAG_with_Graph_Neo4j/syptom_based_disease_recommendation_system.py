import os
from openai import OpenAI
from neo4j import GraphDatabase, basic_auth
from dotenv import load_dotenv

load_dotenv()

# OpenAI setup
token = os.getenv('GITHUB_TOKEN')  # GitHub Marketplace Token
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Neo4j connection
NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

# Query Neo4j for relevant information
def query_neo4j(symptom):
    with driver.session(database="healthcare") as session:
        query = """
        MATCH (s:Symptom)-[:INDICATES]->(d:Disease)
        WHERE s.name = $symptom
        RETURN d.name AS disease, d.description AS description
        """
        result = session.run(query, symptom=symptom)
        return [{"disease": record["disease"], "description": record["description"]} for record in result]


# Generate response using OpenAI API
def generate_llm_response(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a bot that provides medical recommendations based on symptoms."},
            {"role": "user", "content": prompt}
        ],
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model_name
    )
    return response.choices[0].message.content

# Main function to process symptoms and provide recommendations
def get_disease_recommendations(symptom):
    diseases = query_neo4j(symptom)
    if not diseases:
        return f"No diseases found for the symptom: {symptom}"

    disease_info = "\n".join([f"{d['disease']}: {d['description']}" for d in diseases])
    prompt = f"The patient is experiencing {symptom}. These diseases are relevant:\n{disease_info}\nProvide recommendations."

    return generate_llm_response(prompt)

# Example usage
symptom = "Fever"
response = get_disease_recommendations(symptom)
print(response)
