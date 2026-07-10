from problem1_rag.app.models.retrieval_result import RetrievalResult
from problem1_rag.app.prompt.prompt_builder import PromptBuilder

def test_prompt_builder():
    context = [
        RetrievalResult(
            text="Retrieval-Augmented Generation combines retrieval with LLMs.",
            source="sample.md",
            file_type=".md",
            chunk_index=0,
            distance=0.15,
        )
    ]

    prompt = PromptBuilder.build(
        question="What is RAG?",
        context=context,
    )

    assert "What is RAG?" in prompt
    assert "Retrieval-Augmented Generation" in prompt
    assert "sample.md" in prompt