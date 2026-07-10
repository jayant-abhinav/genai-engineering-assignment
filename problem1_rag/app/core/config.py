from pathlib import Path

# Project Paths
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

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