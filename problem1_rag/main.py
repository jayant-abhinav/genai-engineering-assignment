from fastapi import FastAPI
from problem1_rag.app.api.routes import router

app = FastAPI(
    title="GenAI Engineering Assignment",
    version="1.0.0",
    description="Problem 1 - RAG System",
)

app.include_router(router)