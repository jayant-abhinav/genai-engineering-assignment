from chromadb import PersistentClient
from problem1_rag.app.core.config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_DB_DIR,
)

class ChromaStore:
    """
    Handles persistent storage and retrieval of document embeddings using ChromaDB.
    """

    def __init__(self):

        self.client = PersistentClient(
            path=str(CHROMA_DB_DIR)
        )

        self.collection = self.client.get_or_create_collection(
            name=CHROMA_COLLECTION_NAME
        )
    
    def count(self) -> int:
        """
        Return the number of stored chunks.
        """
        return self.collection.count()


    def reset(self):
        """
        Delete all vectors from the collection.
        """
        self.client.delete_collection(CHROMA_COLLECTION_NAME)

        self.collection = self.client.get_or_create_collection(
            name=CHROMA_COLLECTION_NAME
        )