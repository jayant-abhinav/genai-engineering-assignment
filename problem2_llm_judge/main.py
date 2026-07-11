# Entry point for the Problem 2 LLM Judge service.
from fastapi import FastAPI
from problem2_llm_judge.core.config import get_settings
from problem2_llm_judge.core.logging import configure_logging

settings = get_settings()
configure_logging(settings.LOG_LEVEL)

app = FastAPI(
    title="Problem 2 - LLM Judge",
    version="1.0.0",
    description="LLM-based response evaluation service."
)

@app.get("/health", tags=["Health"])
def health() -> dict[str, str]:
    # Health check endpoint.
    return {
        "status": "healthy",
        "service": "problem2_llm_judge",
    }