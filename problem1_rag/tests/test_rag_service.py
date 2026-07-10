from unittest.mock import Mock
from problem1_rag.app.models.rag_response import RAGResponse
from problem1_rag.app.models.retrieval_result import RetrievalResult
from problem1_rag.app.rag.rag_service import RAGService

def test_rag_service():

    embedding = Mock()
    retriever = Mock()
    prompt_builder = Mock()
    llm = Mock()

    embedding.embed_query.return_value = [0.1, 0.2]

    retrieval = []
    retriever.retrieve.return_value = [
        RetrievalResult(
            text="Example",
            source="sample.md",
            file_type=".md",
            chunk_index=0,
            distance=0.1,
        )
    ]

    prompt_builder.build.return_value = "Prompt"
    llm.generate.return_value = "Answer"

    rag = RAGService(
        embedding,
        retriever,
        prompt_builder,
        llm,
    )

    result = rag.answer("Hello")

    assert isinstance(result, RAGResponse)
    assert result.answer == "Answer"