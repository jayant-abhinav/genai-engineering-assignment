from pathlib import Path
from problem1_rag.app.chunking.chunker import Chunker
from problem1_rag.app.core.config import (
    RAW_DATA_DIR,
    SUPPORTED_EXTENSIONS,
)
from problem1_rag.app.embeddings.embedding_service import EmbeddingService
from problem1_rag.app.ingestion.document_loader import load_document
from problem1_rag.app.vectorstore.vector_store import ChromaStore

def ingest():

    vector_store = ChromaStore()
    vector_store.reset()
    
    print("Knowledge base reset.")
    print(f"Current vectors: {vector_store.count()}")

    documents = []
    for path in RAW_DATA_DIR.rglob("*"):

        if(path.is_file()and path.suffix.lower() in SUPPORTED_EXTENSIONS):
            print(f"Loading {path.name}")

            documents.append(
                load_document(path)
            )

    print(f"\nLoaded {len(documents)} documents")

    chunker = Chunker()
    chunks = chunker.chunk_documents(documents)

    print(f"Created {len(chunks)} chunks")

    embedding_service = EmbeddingService()
    embeddings = embedding_service.embed_chunks(chunks)

    print("Embeddings generated")

    vector_store.add_embeddings(
        chunks,
        embeddings,
    )

    print(f"Total vectors in Chroma: {vector_store.count()}")
    print("\nKnowledge base successfully indexed.")


if __name__ == "__main__":
    ingest()