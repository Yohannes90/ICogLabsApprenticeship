# Training Week 9: Search Engine with Lemmatization, TF-IDF, and Cosine Similarity

## Overview

This document covers the Week 9 assignment for building a simple search engine that leverages **Lemmatization**, **TF-IDF**, and **Cosine Similarity** to analyze and retrieve relevant documents based on user input. The assignment involves improving a search system by addressing an issue with the search for the word “loved” and creating a **web-based search system**.

For more details on the training content, refer to the training notebook:
**[1. Training: Search_Engine_with_Lemmatization,_TF_IDF,_and_Cosine_Similarity.ipynb](1.%20Training:%20Search_Engine_with_Lemmatization,_TF_IDF,_and_Cosine_Similarity.ipynb)**


## Assignment Questions

### Assignment 1: Issue with "Love"/"Loved"
In this part of the assignment, we were tasked with investigating and fixing an issue where the search for “loved” did not return the expected results. This was due to preprocessing steps that affected the similarity calculation. The fix involved using a lemmatization technique to ensure that both "love" and "loved" are treated similarly, enhancing the search functionality.

- **Answer and Details:** The complete solution and implementation for this assignment can be found in the file:
  **[2. Assignment 1: Search_Engine_with_Lemmatization,_TF_IDF,_and_Cosine_Similarity.ipynb](2.%20Assignment%201:%20Search_Engine_with_Lemmatization,_TF_IDF,_and_Cosine_Similarity.ipynb)**


### Assignment 2: Web-Based Search System
The goal of this assignment was to build a **web-based search system** that allows users to input search queries and retrieve relevant documents from various sources, such as PDFs, Word documents, or websites. The system uses **TF-IDF** to rank the results based on their relevance to the query, and users can adjust the number of top results returned. Additionally, the system displays the similarity score of each result.

#### Features:
- **Dynamic Content:** Users can upload files or add web links to the search corpus.
- **TF-IDF Ranking:** Search results are ranked based on their relevance to the query.
- **Similarity Scores:** The system displays similarity scores for retrieved documents.

- **Answer and Details:** Full details about the web-based system are provided in the system’s documentation:
  **[search_system/README.md](search_system/README.md)**

## Folder Structure

```
|-- 1. Training: Search_Engine_with_Lemmatization,_TF_IDF,_and_Cosine_Similarity.ipynb
|-- 2. Assignment 1: Search_Engine_with_Lemmatization,_TF_IDF,_and_Cosine_Similarity.ipynb
|-- README.md
|-- search_system
|   |-- app.py                      # Flask app entry point
|   |-- routes.py                   # Routes for handling requests
|   |-- utils.py                    # Utility functions (e.g., preprocessing, scraping)
|   |-- static/
|   |   `-- index.html              # Static front-end for search system
|   |-- uploads/
|   |-- README.md
```
