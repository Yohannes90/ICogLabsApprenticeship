# Task 2 - Improve Your RAG's to use better similarity method, use vector database...(Version 2)

## Overview

This project is an enhanced version of the **Retrieval-Augmented Generation (RAG)** system. It combines document similarity computation using **sentence embeddings** with **ChromaDB** and GPT to generate activity recommendations based on user input.

---

## Features

1. **ChromaDB Integration**: Efficient indexing and querying of a predefined activity corpus.
2. **Sentence Embedding Model**: Uses a transformer-based model for accurate similarity scoring.
3. **GPT Integration**: Generates human-friendly activity recommendations.
4. **Dynamic Ranking**: Ranks activities based on relevance to the user's query.

---

## Prerequisites

- Python 3.8+

---

## Setup and Run

1. Clone the repository and navigate to the project folder:
   ```bash
   git clone https://github.com/Yohannes90/training.git
   cd training/task_2_build_own_RAG_system/
   ```
2. Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   GITHUB_TOKEN=your_openai_api_key
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the script:
   ```bash
   python v2_rag_script.py
   ```
6. Follow the interactive prompts:
   - Input your activity preference when asked.
   - View similarity-based activity rankings and GPT-generated recommendations.

---

## Improvements Over Version 1

- Integrated **ChromaDB** for scalable document indexing and retrieval.
- Replaced Jaccard similarity with **cosine similarity** using sentence embeddings for more accurate activity matching.
- Improved user prompts and GPT-based recommendation clarity.

---

## Next Steps

- Expand the activity corpus.
- Enhance GPT prompt engineering for nuanced recommendations.
- Experiment with other embedding models for diverse use cases.

---

### Resources Used

This project drew inspiration from the following:

1. [LearnByBuilding: RAG from Scratch](https://learnbybuilding.ai/tutorials/rag-from-scratch)
2. [LearnByBuilding: Semantics and Cosine Similarity](https://learnbybuilding.ai/tutorials/rag-from-scratch-part-2-semantics-and-cosine-similarity)
3. [Kaggle Notebook: RAG with Vector DB and LLMs](https://www.kaggle.com/code/aisuko/rag-by-leveraging-vector-db-and-llms)
4. [YouTube Tutorial: RAG Concepts](https://youtu.be/bmduzd1oY7U?si=JzwNOjGhP7g_0dnE)
5. [YouTube Tutorial: RAG Techniques](https://youtu.be/bmduzd1oY7U?si=4nUtZOZy37kVUS81)

Gratitude to the creators for their valuable contributions.

---
