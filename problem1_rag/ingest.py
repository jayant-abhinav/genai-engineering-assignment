import argparse
from pathlib import Path
from problem1_rag.app.chunking.chunker import Chunker
from problem1_rag.app.core.config import (
    EVAL_DATA_DIR, SUPPORTED_EXTENSIONS,
)
from problem1_rag.app.embeddings.embedding_service import EmbeddingService
from problem1_rag.app.ingestion.document_loader import load_document
from problem1_rag.app.vectorstore.vector_store import ChromaStore

def parse_args():
    parser = argparse.ArgumentParser(
        description="Index documents into ChromaDB."
    )

    parser.add_argument(
        "--input-dir",
        type=Path,
        default=EVAL_DATA_DIR,
        help="Directory containing PDF, DOCX, TXT, HTML and Markdown files.",
    )

    parser.add_argument(
        "--chunk-size",
        type=int,
        default=800,
        help="Chunk size in characters.",
    )

    parser.add_argument(
        "--chunk-overlap",
        type=int,
        default=100,
        help="Chunk overlap in characters.",
    )

    parser.add_argument(
        "--reset-db",
        action="store_true",
        help="Reset the Chroma collection before ingestion.",
    )
    return parser.parse_args()

def ingest():

    args = parse_args()
    vector_store = ChromaStore()
    if args.reset_db:
        vector_store.reset()
        print("Knowledge base reset.")
    
    print(f"Current vectors: {vector_store.count()}")

    documents = []
    for path in args.input_dir.rglob("*"):

        if(path.is_file()and path.suffix.lower() in SUPPORTED_EXTENSIONS):
            print(f"Loading {path.name}")

            documents.append(
                load_document(path)
            )

    print(f"\nLoaded {len(documents)} documents")

    chunker = Chunker(chunk_size=args.chunk_size, chunk_overlap=args.chunk_overlap,)
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