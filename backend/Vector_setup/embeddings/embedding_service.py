# embedding_service.py
from typing import List
from sentence_transformers import SentenceTransformer
import logging

logger = logging.getLogger(__name__)

class EmbeddingService:
    def __init__(self, model_name):
        self.model_name = model_name
        logger.info("Loading embedding model: %s", self.model_name)
        self._model = SentenceTransformer(self.model_name)

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        embeddings = self._model.encode(
            texts,
            batch_size=32,
            show_progress_bar=False,
        ).tolist()

        if (
            not isinstance(embeddings, list)
            or len(embeddings) == 0
            or not isinstance(embeddings[0], list)
            or len(embeddings[0]) == 0
        ):
            logger.warning("Invalid embeddings: %s", embeddings)
            return []

        return embeddings
