from problem1_rag.app.vectorstore.vector_store import ChromaStore
from pathlib import Path
from problem1_rag.app.models.chunk import DocumentChunk
from problem1_rag.app.vectorstore.vector_store import ChromaStore
from problem1_rag.app.embeddings.embedding_service import EmbeddingService

def test_chroma_initialization():

    store = ChromaStore()

    assert store.collection is not None
    assert store.count() >= 0

def test_add_embeddings():

    store = ChromaStore()
    store.reset()

    chunks = [
        DocumentChunk(
            chunk_id="chunk1",
            source=Path("sample.md"),
            file_type=".md",
            text="Artificial Intelligence",
            chunk_index=0,
            metadata={},
        )
    ]

    embeddings = [[0.0] * 384]
    store.add_embeddings(chunks,embeddings,)

    assert store.count() == 1

def test_similarity_search():

    store = ChromaStore()
    store.reset()
    service = EmbeddingService()

    chunks = [

        DocumentChunk(
            chunk_id="chunk1",
            source=Path("sample.md"),
            file_type=".md",
            text="Artificial Intelligence is transforming software engineering.",
            chunk_index=0,
            metadata={},
        ),

        DocumentChunk(
            chunk_id="chunk2",
            source=Path("sample.md"),
            file_type=".md",
            text="Python is a popular programming language.",
            chunk_index=1,
            metadata={},
        ),

    ]

    embeddings = service.embed_chunks(chunks)
    store.add_embeddings(chunks, embeddings,)

    query = service.embed_text(
        "What is Artificial Intelligence?"
    )

    results = store.similarity_search(
        query_embedding=query,
        k=1,
    )

    assert len(results["documents"][0]) == 1
    assert "Artificial Intelligence" in results["documents"][0][0]