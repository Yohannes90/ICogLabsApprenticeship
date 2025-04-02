import os
import re
import nltk
import requests
from docx import Document
from PyPDF2 import PdfReader
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup


# Initialize NLP Tools
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('averaged_perceptron_tagger_eng')

lemmer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def preprocess(text):
    """Preprocess text for analysis."""
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
    text = re.sub(r'[0-9]', '', text)  # Remove numbers
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)  # Remove punctuation
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text.strip()


def chunk_text(text, chunk_size=50):
    """Split text into chunks of a given size."""
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]


def get_wordnet_pos(word):
    """Map POS tag to WordNet POS format."""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    return {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}.get(tag, wordnet.NOUN)


def lemmatize_documents(documents):
    """Lemmatize each word in the documents."""
    return [' '.join([lemmer.lemmatize(word, get_wordnet_pos(word)) for word in doc.split()]) for doc in documents]


def extract_text_from_file(file_path):
    """Extract text from .txt, .docx, or .pdf files."""
    _, ext = os.path.splitext(file_path.lower())

    if ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif ext == '.docx':
        doc = Document(file_path)
        return "\n".join(para.text for para in doc.paragraphs)
    elif ext == '.pdf':
        reader = PdfReader(file_path)
        return "".join(page.extract_text() for page in reader.pages)
    else:
        raise ValueError("Unsupported file format. Use .txt, .docx, or .pdf.")


def scrape_website_content(url):
    """Scrape content from a website and extract as much meaningful text as possible."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove unnecessary elements
        for tag in soup(['script', 'style', 'noscript', 'footer', 'header', 'nav']):
            tag.decompose()

        # Extract meaningful content
        content_blocks = []
        for tag in ['p', 'div', 'span', 'article', 'section']:
            for element in soup.find_all(tag):
                text = element.get_text(strip=True)
                if len(text) > 30:  # Avoid very short, non-informative text
                    content_blocks.append(preprocess(text))

        # Join all content into a single string
        return " ".join(content_blocks) if content_blocks else "No meaningful content found."

    except requests.exceptions.RequestException as e:
        return f"Error scraping website: {str(e)}"


def calculate_similarity(query, documents, vectorizer):
    """Get the most similar articles based on cosine similarity."""
    query_vec = vectorizer.transform([query]).toarray()
    doc_vectors = vectorizer.transform(documents).toarray()
    return cosine_similarity(query_vec, doc_vectors).flatten()
