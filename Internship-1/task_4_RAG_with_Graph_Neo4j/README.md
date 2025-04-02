# Task4 - Build a RAG that uses Graph database like neo4j (Symptom-Based Disease Recommendation System)

## Overview

**Symptom-Based Disease Recommendation System** is a small python based application that integrates with Neo4j and OpenAI to provide disease recommendations based on user-reported symptoms. It leverages the power of graph databases to query symptom-disease relationships and uses OpenAI's GPT-based model to generate detailed medical advice.

## Features

- **Symptom Analysis**: Queries a Neo4j database to retrieve diseases related to specific symptoms.
- **AI-Generated Recommendations**: Uses OpenAI's GPT model to provide personalized recommendations based on the queried diseases.
- **Example Usage**: Demonstrates the process using "Fever" as a symptom.

## Prerequisites

1. **Python**: Version 3.8 or higher.
2. **Neo4j Database**:
   - Database name: `healthcare`
   - Relationship schema: `(Symptom)-[:INDICATES]->(Disease)`
3. **OpenAI API**: An active API key and endpoint.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Yohannes90/training.git
   cd training/task_4_RAG_with_Graph_Neo4j/
   ```

2. Install dependencies:
   ```bash
   pip install neo4j openai python-dotenv
   ```

3. Create a `.env` file in the project directory with the following content:
   ```env
   GITHUB_TOKEN=your_github_token
   NEO4J_URI=bolt://your_neo4j_uri
   NEO4J_USERNAME=your_neo4j_username
   NEO4J_PASSWORD=your_neo4j_password
   ```

## Replicating the Database

To replicate the database schema and populate some initial data, run the following Cypher commands in your Neo4j browser:

### Cypher Command for Creating Nodes and Relationships

```cypher
CREATE (:Patient {name: "John Doe", age: 45, gender: "Male"});
CREATE (:Patient {name: "Jane Smith", age: 30, gender: "Female"});
CREATE (:Symptom {name: "Fever"});
CREATE (:Symptom {name: "Cough"});
CREATE (:Symptom {name: "Chest Pain"});
CREATE (:Disease {name: "Flu", description: "Viral infection affecting respiratory system"});
CREATE (:Disease {name: "Pneumonia", description: "Infection that inflames air sacs in the lungs"});
CREATE (:Medication {name: "Antiviral Drug"});
CREATE (:Medication {name: "Antibiotics"});
CREATE (:Doctor {name: "Dr. Alice", specialty: "Pulmonology"});
CREATE (:Doctor {name: "Dr. Bob", specialty: "Internal Medicine"});
CREATE (:Hospital {name: "City Hospital"});
CREATE (:Test {name: "Chest X-Ray"});
CREATE (:Test {name: "PCR Test"});
CREATE (:Lifestyle {factor: "Smoking"});
CREATE (:Lifestyle {factor: "Exercise"});


CREATE (p:Patient {name: "John Doe"})-[:HAS_SYMPTOM]->(s:Symptom {name: "Fever"});
CREATE (p:Patient {name: "John Doe"})-[:HAS_SYMPTOM]->(s:Symptom {name: "Cough"});
CREATE (s:Symptom {name: "Fever"})-[:INDICATES]->(d:Disease {name: "Flu"});
CREATE (s:Symptom {name: "Chest Pain"})-[:INDICATES]->(d:Disease {name: "Pneumonia"});
CREATE (d:Disease {name: "Flu"})-[:TREATED_BY]->(m:Medication {name: "Antiviral Drug"});
CREATE (d:Disease {name: "Pneumonia"})-[:TREATED_BY]->(m:Medication {name: "Antibiotics"});
CREATE (doc:Doctor {name: "Dr. Alice"})-[:WORKS_AT]->(h:Hospital {name: "City Hospital"});
CREATE (doc:Doctor {name: "Dr. Alice"})-[:SPECIALIZES_IN]->(d:Disease {name: "Pneumonia"});
CREATE (l:Lifestyle {factor: "Smoking"})-[:AFFECTS]->(d:Disease {name: "Pneumonia"});
CREATE (d:Disease {name: "Pneumonia"})-[:DIAGNOSED_BY]->(t:Test {name: "Chest X-Ray"});


MATCH (d:Disease {name: "Flu"})
SET d.description = "A contagious respiratory illness caused by influenza viruses."
RETURN d;

MATCH (d:Disease {name: "Cold"})
SET d.description = "A viral infection of the upper respiratory tract."
RETURN d;

MATCH (d:Disease {name: "Malaria"})
SET d.description = "A mosquito-borne disease caused by Plasmodium parasites."
RETURN d;

MATCH (d:Disease {name: "Typhoid"})
SET d.description = "A bacterial infection due to Salmonella typhi, spread through contaminated food or water."
RETURN d;

MATCH (d:Disease {name: "Dengue"})
SET d.description = "A mosquito-borne viral disease causing severe flu-like illness."
RETURN d;

MATCH (d:Disease {name: "Covid-19"})
SET d.description = "An infectious disease caused by the SARS-CoV-2 virus."
RETURN d;

MATCH (d:Disease {name: "Pneumonia"})
SET d.description = "An infection that inflames the air sacs in one or both lungs."
RETURN d;

```

## Usage

1. **Set Up Environment Variables**:
   - Ensure the `.env` file is set up with your credentials as described above.

2. **Run the Application**:
   - Execute the script:
     ```bash
     python task_4_RAG_with_Graph_Neo4j.py
     ```
   - The script will query the database for diseases related to the symptom "Fever" and generate recommendations.

## Code Explanation

1. **Neo4j Query Function**:
   - Queries the `healthcare` database for diseases associated with a given symptom.

2. **OpenAI Integration**:
   - Generates detailed recommendations based on queried diseases using a GPT-based model.

3. **Main Function**:
   - Combines Neo4j query results with AI-generated responses to provide actionable insights.

## Example Output

For the symptom `Fever`, the application might produce:
```bash
(venv) yohannes@Xubuntu-22:~/Desktop/icog_related/week_1_training_ECAN/task_4_RAG_with_Graph_Neo4j$ python3 syptom_based_disease_recommendation_system.py
```
```plaintext
For a patient experiencing fever with the possibility of having the flu, here are some general recommendations:

1. **Rest**: Encourage the patient to get plenty of rest to help the body fight off the infection.

2. **Hydration**: Ensure the patient stays well-hydrated. Recommend drinking water, herbal teas, or clear broths to prevent dehydration.

3. **Over-the-Counter Medications**: Consider the use of over-the-counter medications such as acetaminophen or ibuprofen to reduce fever and alleviate body aches. Make sure to follow dosing instructions on the package.

4. **Symptom Management**: Additional OTC medications may help alleviate other flu symptoms, such as cough suppressants or decongestants, if applicable.

5. **Monitor Symptoms**: Advise the patient to monitor their symptoms. If the fever persists for more than a few days, or if they develop severe symptoms such as difficulty breathing, chest pain, or persistent vomiting, they should seek medical attention.

6. **Isolation**: Encourage the patient to limit contact with others to prevent spreading the virus, especially if they are experiencing respiratory symptoms.

7. **Consult a Healthcare Provider**: If the patient has underlying health conditions, is very young or elderly, or if symptoms worsen, they should consult a healthcare provider for further evaluation and possible antiviral medication.

8. **Flu Vaccine**: If this is the flu and the patient has not yet been vaccinated, discuss the importance of getting the flu vaccine to prevent future infections.

Always remind patients to seek personalized medical advice from their healthcare provider based on their specific health history and conditions.

```
