
# Task 1 - Read About RAGs and Build Your Own RAG (Version 1)

## Overview
This project demonstrates a simple implementation of **Retrieval-Augmented Generation (RAG)**, combining document similarity scoring (using Jaccard similarity) and OpenAI's GPT model to recommend activities based on user input.

---

## Features
1. **Jaccard Similarity Function**: Identifies the most relevant activity from a predefined corpus based on user input.
2. **OpenAI API Integration**: Generates user-friendly recommendations for activities.
3. **Corpus of Activities**: Includes detailed descriptions of diverse activities for personalized suggestions.

---

## How to Run

### Prerequisites
- Python 3.8+
- OpenAI Python SDK (`openai`)
- Python Dotenv (`python-dotenv`)

### Installation
1. Clone the repository and navigate to the project folder.
2. Install dependencies:
   ```bash
   pip install openai python-dotenv
   ```
3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   GITHUB_TOKEN=your_openai_api_key
   ```

### Running the Program
1. Run the script:
   ```bash
   python v1_simple_rag_with_openai.py
   ```
2. Input your desired activity when prompted.
3. View the generated recommendation based on the most relevant activity from the corpus.

---

## Next Steps
- Learn more about **RAGs** to improve document retrieval and response generation.
- Expand the corpus for diverse activities.
- Experiment with alternative similarity measures for enhanced matching.

---
