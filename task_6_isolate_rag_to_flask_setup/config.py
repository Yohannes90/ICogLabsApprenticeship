import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    QDRANT_CLIENT = os.getenv('QDRANT_CLIENT', 'http://localhost:6333')
    COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'default_collection')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
