from dataclasses import dataclass
from problem1_rag.app.models.retrieval_result import RetrievalResult
@dataclass(slots=True)
class RAGResponse:

    #  Final response returned by the RAG pipeline.
    answer: str
    retrieval: RetrievalResult