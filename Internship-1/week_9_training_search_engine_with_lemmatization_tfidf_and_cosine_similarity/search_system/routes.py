from app import app
from flask import request, jsonify
from werkzeug.utils import secure_filename
import os
from utils import preprocess, chunk_text, lemmatize_documents, extract_text_from_file, scrape_website_content, calculate_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords, wordnet


# Initialize Corpus
corpus = []


# Route for the home page
@app.route('/')
def index():
    return app.send_static_file('index.html')


# Route for adding to the corpus (via text, file, or website)
@app.route('/corpus/add', methods=['POST'])
def add_corpus_item():
    """Add text, file, or website content to the corpus."""
    data = request.form
    file = request.files.get('file')
    url = data.get('url')
    title = data.get('title', 'From Text Input')

    no_text_input_id = 0
    if text := data.get('text'):
        no_text_input_id += 1
        title = title + str(no_text_input_id)
        add_to_corpus(text, source=title, method="Text Input")
        return jsonify({"message": "Text added to corpus!", "title": title, "method": "Text Input"}), 201

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(file_path)

        try:
            content = extract_text_from_file(file_path)
            add_to_corpus(content, source=filename, method="File Upload")
            return jsonify({"message": "File added to corpus!", "title": filename, "method": "File Upload"}), 201
        except Exception as e:
            return jsonify({"error": f"Error processing file: {str(e)}"}), 400

    if url:
        content = scrape_website_content(url)
        add_to_corpus(content, source=url, method="Web Scraping")
        return jsonify({"message": "Website content added to corpus!", "url": url, "method": "Web Scraping"}), 201

    return jsonify({"error": "No valid input provided."}), 400


# Route for fetching the corpus
@app.route('/corpus', methods=['GET'])
def get_corpus():
    """Fetch all items in the corpus, but list only file names/URLs."""
    # Create a list of unique sources (file names or URLs) without repeating chunk IDs
    unique_sources = []
    for item in corpus:
        if not any(d['source'] == item['source'] for d in unique_sources):
            unique_sources.append({
                "source": item["source"],
                "method": item["method"],
                "chunk": item["text"],
                "chunk_id": item["chunk_id"],
                "chunk_count": sum(1 for x in corpus if x["source"] == item["source"])
            })
    return jsonify(unique_sources), 200


# Route for removing a specific item by source
@app.route('/corpus/remove/<path:source>', methods=['DELETE'])
def remove_corpus_item_by_source(source):
    """Remove all items from the corpus by their source."""
    global corpus
    items_to_remove = [item for item in corpus if item["source"] == source]

    if items_to_remove:
        corpus = [item for item in corpus if item["source"] != source]
        return jsonify({"message": f"Removed {len(items_to_remove)} items from source '{source}'."}), 200
    else:
        return jsonify({"error": "Source not found."}), 404


# Route for searching the corpus
@app.route('/search', methods=['POST'])
def search_corpus():
    """Search for similar text within the corpus and return top results."""
    data = request.json
    query = data.get("query", "")
    limit = int(data.get("limit", 10))

    # Validate input
    if not query:
        return jsonify({"error": "Query cannot be empty."}), 400

    if not corpus:
        return jsonify({"error": "The corpus is empty. Please add data to the corpus and try again."}), 400

    processed_query = preprocess(query)
    lemmatized_query = lemmatize_documents([processed_query])[0]

    corpus_texts = [item["text"] for item in corpus]

    vectorizer = TfidfVectorizer(analyzer='word',
                                 ngram_range=(1, 2),
                                 min_df=0.002,
                                 max_df=0.99,
                                 max_features=10000,
                                 lowercase=True,
                                 stop_words=stopwords.words('english'))
    vectorizer.fit(corpus_texts)
    similarities = calculate_similarity(lemmatized_query, corpus_texts, vectorizer)

    results = []
    for idx, score in sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)[:limit]:
        corpus_item = corpus[idx]
        source = corpus_item["source"]
        chunk_count = sum(1 for item in corpus if item["source"] == source)

        if score > 0:
            results.append({
                "source": source,
                "method": corpus_item["method"],
                "chunk_id": corpus_item["chunk_id"],
                "similarity_score": round(score, 4),
                "chunk": corpus_item["text"],
                "chunk_count": chunk_count
            })
    if not results:
        return jsonify({"message": "No similar text found in the corpus for the given query."}), 200

    return jsonify(results), 200


def add_to_corpus(text, source, method):
    """Add processed text to the corpus."""
    chunks = chunk_text(text)
    processed_chunks = [preprocess(chunk) for chunk in chunks]
    lemmatized_chunks = lemmatize_documents(processed_chunks)

    for idx, chunk in enumerate(lemmatized_chunks):
        corpus.append({
            "source": source,
            "method": method,
            "text": chunk,
            "chunk_id": idx + 1
        })
