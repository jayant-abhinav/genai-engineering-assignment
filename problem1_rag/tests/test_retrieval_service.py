from problem1_rag.app.embeddings.embedding_service import EmbeddingService
from problem1_rag.app.retrieval.retriever import Retriever
from problem1_rag.app.vectorstore.vector_store import ChromaStore

def test_retrieval():

    embedding_service = EmbeddingService()
    vector_store = ChromaStore()
    retriever = Retriever(vector_store)

    query_embedding = embedding_service.embed_text(
        "Explain Retrieval-Augmented Generation"
    )

    results = retriever.retrieve(
        query_embedding=query_embedding,
        k=1,
    )

    assert len(results) == 1
    assert results[0].text != ""
    assert results[0].source == "sample.md"
    assert isinstance(results[0].distance, float)