import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Project Paths
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
EVAL_DATA_DIR = DATA_DIR / "evaluation_docs"

LOG_DIR = BASE_DIR / "logs"

# Supported File Types
SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".html",
    ".md",
}

# Chunking Configuration
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Embedding Configuration
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = LOG_DIR / "rag_pipeline.log"

# ChromaDB Configuration
CHROMA_DB_DIR = BASE_DIR / "chroma_db"
CHROMA_COLLECTION_NAME = "documents"

# Gemini Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

# Retry Configuration
LLM_MAX_RETRIES = 3
LLM_RETRY_MIN_WAIT = 1
LLM_RETRY_MAX_WAIT = 8
TOP_K_RESULTS = 5