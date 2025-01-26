# app.py
from flask import Flask
from flask_cors import CORS
import nltk


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
CORS(app)


from routes import *


# Initialize NLP Tools
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('averaged_perceptron_tagger_eng')


if __name__ == "__main__":
    app.run(debug=True)
