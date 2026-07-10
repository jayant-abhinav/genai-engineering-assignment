from typing import List
from sentence_transformers import SentenceTransformer
from problem1_rag.app.core.config import EMBEDDING_MODEL
from problem1_rag.app.models.chunk import DocumentChunk

class EmbeddingService:
  
    # Generates embeddings for document chunks using SentenceTransformers.
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed_text(self, text: str) -> List[float]:

        # Generate embedding for a single text.
        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        return embedding.tolist()

    def embed_chunks(self, chunks: List[DocumentChunk],) -> List[List[float]]:

        # Generate embeddings for multiple chunks.
        texts = [chunk.text for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True,
        )
        return embeddings.tolist()