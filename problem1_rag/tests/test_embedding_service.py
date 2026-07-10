from pathlib import Path
from problem1_rag.app.embeddings.embedding_service import EmbeddingService
from problem1_rag.app.models.chunk import DocumentChunk

def test_embed_text():

    # Test embedding generation for a single text.
    service = EmbeddingService()
    embedding = service.embed_text("Hello World")

    assert isinstance(embedding, list)
    assert len(embedding) == 384


def test_embed_chunks():

    # Test embedding generation for multiple chunks.
    service = EmbeddingService()
    chunks = [
        DocumentChunk(
            chunk_id="1",
            source=Path("sample.md"),
            file_type=".md",
            text="Artificial Intelligence",
            chunk_index=0,
            metadata={},
        ),
        DocumentChunk(
            chunk_id="2",
            source=Path("sample.md"),
            file_type=".md",
            text="Machine Learning",
            chunk_index=1,
            metadata={},
        ),
    ]

    embeddings = service.embed_chunks(chunks)

    assert len(embeddings) == 2
    assert len(embeddings[0]) == 384
    assert len(embeddings[1]) == 384