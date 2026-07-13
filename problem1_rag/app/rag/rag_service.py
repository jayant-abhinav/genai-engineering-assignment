from problem1_rag.app.embeddings.embedding_service import EmbeddingService
from problem1_rag.app.llm.llm_service import LLMService
from problem1_rag.app.models.rag_response import RAGResponse
from problem1_rag.app.prompt.prompt_builder import PromptBuilder
from problem1_rag.app.retrieval.retriever import Retriever
class RAGService:
    """
    Orchestrates the complete RAG pipeline.

    Responsibilities:
    - Generate query embedding
    - Retrieve relevant chunks
    - Build grounded prompt
    - Generate final answer using the LLM
    """

    def __init__(
        self,
        embedding_service: EmbeddingService,
        retriever: Retriever,
        prompt_builder: PromptBuilder,
        llm: LLMService,
    ):
        self.embedding_service = embedding_service
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm = llm

    def answer(self, query: str) -> RAGResponse:

        # Execute the complete RAG pipeline.
        # Step 1: Embed query
        query_embedding = self.embedding_service.embed_query(query)
   
        # Step 2: Retrieve relevant chunks
        retrieval_result = self.retriever.retrieve(query_embedding)

        # Step 3: Build prompt
        prompt = self.prompt_builder.build(
            question=query,
            context=retrieval_result,
        )

        # Step 4: Generate answer
        answer = self.llm.generate(prompt)

        return RAGResponse(
            answer=answer,
            retrieval=retrieval_result,
        )
        