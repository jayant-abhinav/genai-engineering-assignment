from functools import lru_cache
from problem1_rag.app.embeddings.embedding_service import EmbeddingService
from problem1_rag.app.llm.gemini_llm import GeminiLLM
from problem1_rag.app.prompt.prompt_builder import PromptBuilder
from problem1_rag.app.rag.rag_service import RAGService
from problem1_rag.app.retrieval.retriever import Retriever
from problem1_rag.app.vectorstore.vector_store import ChromaStore
from problem1_rag.app.core.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)

@lru_cache
def get_rag_service() -> RAGService:

    # Creates a singleton RAG service.
    vector_store = ChromaStore()
    embedding_service = EmbeddingService()
    retriever = Retriever(vector_store)
    prompt_builder = PromptBuilder()

    llm = GeminiLLM(
        api_key=GEMINI_API_KEY,
        model_name=GEMINI_MODEL,
    )

    return RAGService(
        embedding_service=embedding_service,
        retriever=retriever,
        prompt_builder=prompt_builder,
        llm=llm,
    )