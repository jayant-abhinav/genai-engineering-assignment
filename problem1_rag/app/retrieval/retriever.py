from typing import List, Optional
from problem1_rag.app.models.retrieval_result import RetrievalResult
from problem1_rag.app.vectorstore.vector_store import ChromaStore
from problem1_rag.app.core.config import TOP_K_RESULTS

class Retriever:
    # Handles semantic retrieval from the vector store.

    def __init__(self, vector_store: ChromaStore):
        self.vector_store = vector_store

    def retrieve(
        self,
        query_embedding: list[float],
        k: int = TOP_K_RESULTS,
        where: Optional[dict] = None,
    ) -> List[RetrievalResult]:

        response = self.vector_store.similarity_search(
            query_embedding=query_embedding,
            k=k,
            where=where,
        )

        results = []

        documents = response["documents"][0]
        metadatas = response["metadatas"][0]
        distances = response["distances"][0]

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances,
        ):
            results.append(
                RetrievalResult(
                    text=document,
                    source=metadata["source"],
                    file_type=metadata["file_type"],
                    chunk_index=metadata["chunk_index"],
                    distance=distance,
                )
            )
        return results