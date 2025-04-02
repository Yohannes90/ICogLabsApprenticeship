from qdrant_client import QdrantClient
from qdrant_client.http import models
import os
from datetime import datetime
import uuid
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VectorStore:
    def __init__(self):
        self.client = QdrantClient(os.getenv('QDRANT_CLIENT', 'http://localhost:6333'))
        self.collection_name = os.getenv('COLLECTION_NAME', 'default_collection')
        self.vector_size = 1536

    def init_collection(self):

        try:
            self.client.get_collection(self.collection_name)
        except:
            logger.info(f"Creating collection {self.collection_name}")
            self.client.create_collection(
                self.collection_name,
                vectors_config=models.VectorParams(
                    size=self.vector_size,
                    distance=models.Distance.DOT
                )
            )

    def upsert_embeddings(self, username, content, embedding):
        try:
            self.init_collection()
            point_id = str(uuid.uuid4())

            self.client.upsert(
                collection_name=self.collection_name,
                points=models.Batch(
                    ids=[point_id],
                    vectors=[embedding],
                    payloads=[{
                        'username': username,
                        'content': content,
                        'created_at': datetime.utcnow().isoformat()
                    }]
                )
            )
            return point_id
        except Exception as e:
            logger.error(f"Error upserting embeddings: {str(e)}")
            raise

    def search_similar(self, username, query_vector, limit=5):
        try:
            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                query_filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="username",
                            match=models.MatchValue(value=username)
                        )
                    ]
                ),
                limit=limit,
                with_payload=True,
                score_threshold=0.3
            )

            return [
                {
                    'content': r.payload['content'],
                    'score': r.score,
                    'created_at': r.payload['created_at']
                } for r in results
            ]
        except Exception as e:
            logger.error(f"Error searching vectors: {str(e)}")
            raise
