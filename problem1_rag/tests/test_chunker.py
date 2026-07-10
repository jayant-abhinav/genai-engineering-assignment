from pathlib import Path
from problem1_rag.app.chunking.chunker import Chunker
from problem1_rag.app.models.document import Document

def test_chunk_document():
    document = Document(
        source=Path("sample.md"),
        file_type=".md",
        text="Hello world. " * 250,
        metadata={}
    )

    chunker = Chunker()
    chunks = chunker.chunk_document(document)

    assert len(chunks) > 1
    assert chunks[0].source == Path("sample.md")
    assert chunks[0].file_type == ".md"
    assert chunks[0].chunk_index == 0