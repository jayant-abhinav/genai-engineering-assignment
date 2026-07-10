from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from problem1_rag.app.api.dependencies import get_rag_service
from problem1_rag.app.api.schemas import (
    AskRequest,
    AskResponse,
    SourceResponse,
)
from problem1_rag.app.rag.rag_service import RAGService
from pathlib import Path
from problem1_rag.app.vectorstore.vector_store import ChromaStore
from problem1_rag.app.core.config import (
    EMBEDDING_MODEL,
    GEMINI_MODEL,
)

router = APIRouter()

@router.get("/health")
def health():

    # Health check endpoint.
    vector_store = ChromaStore()

    return {
        "status": "healthy",
        "vector_count": vector_store.count(),
        "embedding_model": EMBEDDING_MODEL,
        "llm_model": GEMINI_MODEL,
    }

@router.post("/ask", response_model=AskResponse,)
def ask(request: AskRequest, rag_service: RAGService = Depends(get_rag_service),):
    try:
        result = rag_service.answer(request.question)

        seen = set()
        sources = []

        for chunk in result.retrieval:
            filename = Path(chunk.source).name

            if filename in seen:
                continue

            seen.add(filename)
            sources.append(
                SourceResponse(
                    source=filename,
                    chunk_index=chunk.chunk_index,
                )
            )

        return AskResponse(
            answer=result.answer,
            sources=sources,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )

    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while processing the request.",
        )