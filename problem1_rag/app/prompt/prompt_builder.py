from typing import List
from problem1_rag.app.models.retrieval_result import RetrievalResult

class PromptBuilder:

    # Builds grounded prompts for the LLM.
    SYSTEM_PROMPT = (
        "You are a helpful AI assistant.\n"
        "Answer ONLY using the provided context.\n"
        "If the answer cannot be found in the context, "
        "say that the information is not available in the knowledge base.\n"
        "Do not include source citations in the answer text.\n"
        "Sources are returned separately by the application."
    )

    @classmethod
    def build(
        cls,
        question: str,
        context: List[RetrievalResult],
    ) -> str:

        # Build a grounded RAG prompt.
        if not context:
            return (
                f"{cls.SYSTEM_PROMPT}\n\n"
                "Context:\n"
                "No relevant context found.\n\n"
                f"Question:\n{question}\n\n"
                "Answer:"
            )

        context_blocks = []
        for result in context:

            context_blocks.append(
                (
                    f"Source: {result.source}\n"
                    f"Chunk: {result.chunk_index}\n\n"
                    f"{result.text}"
                )
            )

        context_text = "\n\n------------------------\n\n".join(context_blocks)
        return (
            f"{cls.SYSTEM_PROMPT}\n\n"
            f"Context:\n\n{context_text}\n\n"
            f"Question:\n{question}\n\n"
            "Answer:"
        )