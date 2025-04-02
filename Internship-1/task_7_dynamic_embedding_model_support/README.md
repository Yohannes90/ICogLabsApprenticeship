# Task 7: Dynamic Embedding Model Support Integration

## Overview
This document outlines the work completed in **Task 7**, focusing on enhancing the existing **Graph RAG (Retrieval-Augmented Generation)** system. The core objective of this task was to integrate dynamic embedding model support, enabling seamless compatibility with multiple large language model (LLM) providers, specifically **OpenAI** and **Gemini**.

## Key Features
- **Dynamic Embedding Model Support:** Integrated flexible embedding generation capabilities that work efficiently with both OpenAI and Gemini models.
- **Provider-Agnostic Architecture:** Enhanced the system to support easy switching between LLM providers.

## Code Changes Summary
These diffs introduce dynamic embedding model handling and vector size configuration:

- **In `rag.py`:**
  - Imports `gemini_embedding_model`.
  - Adds logic to handle `GeminiModel` with specific `embedding_model` and `embedding_size`.
  - Updates embeddings and reshapes them based on the dynamic `embedding_size`.

- **In `qdrant.py`:**
  - Removes `OPEN_AI_VECTOR_SIZE` constant.
  - Adds logic to set `vector_size` based on the model type (`768` for `GeminiModel`, `1536` otherwise).
  - Updates `create_collection` method to use the dynamically determined `vector_size`.

These changes make the embedding model and vector size adaptable based on the specific model used.

## Repository
- [Pull Request](https://github.com/rejuve-bio/AI-Assistant/pull/24)
- [Main Codebase](https://github.com/rejuve-bio/AI-Assistant/)
- [My Fork](https://github.com/Yohannes90/AI-Assistant/)
