from dataclasses import dataclass
from problem1_rag.app.models.retrieval_result import RetrievalResult

@dataclass(slots=True)
class RAGResponse:
    answer: str
    retrieval: RetrievalResult