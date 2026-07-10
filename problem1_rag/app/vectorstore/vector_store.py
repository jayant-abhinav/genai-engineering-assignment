from chromadb import PersistentClient
from problem1_rag.app.core.config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_DB_DIR,
)
from typing import List
from problem1_rag.app.models.chunk import DocumentChunk
from typing import Optional
class ChromaStore:

    # Handles persistent storage and retrieval of document embeddings using ChromaDB.
    def __init__(self):

        self.client = PersistentClient(
            path=str(CHROMA_DB_DIR)
        )

        self.collection = self.client.get_or_create_collection(
            name=CHROMA_COLLECTION_NAME
        )
    
    def count(self) -> int:

        # Return the number of stored chunks.
        return self.collection.count()

    def reset(self):

        # Delete all vectors from the collection.
        self.client.delete_collection(CHROMA_COLLECTION_NAME)

        self.collection = self.client.get_or_create_collection(
            name=CHROMA_COLLECTION_NAME
        )

    def add_embeddings(self, chunks: List[DocumentChunk], embeddings: List[List[float]], ) -> None:

        # Store document chunks and their embeddings.
        ids = []
        documents = []
        metadatas = []

        for chunk in chunks:
            ids.append(chunk.chunk_id)
            documents.append(chunk.text)

            metadatas.append({
                    "source": str(chunk.source),
                    "file_type": chunk.file_type,
                    "chunk_index": chunk.chunk_index,
                }
            )

        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )
    
    def similarity_search(
        self, 
        query_embedding: list[float], 
        k: int = 5, 
        where: Optional[dict] = None,
        ) -> dict:
        """
        Retrieve the top-k most similar chunks.

        Args:
            query_embedding: Embedding vector of the query.
            k: Number of chunks to retrieve.
            where: Optional metadata filter.

        Returns:
            Raw ChromaDB query result.
        """
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            where=where,
        )

        return results