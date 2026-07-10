from pathlib import Path
from problem1_rag.app.core.config import SUPPORTED_EXTENSIONS
from problem1_rag.app.models.document import Document

from problem1_rag.app.ingestion import (
    html_loader,
    md_loader,
    pdf_loader,
)

LOADERS = {
    ".pdf": pdf_loader.load,
    ".html": html_loader.load,
    ".htm": html_loader.load,
    ".md": md_loader.load,
}

def load_document(path: Path) -> Document:
    
    # Load a document using the appropriate loader.
    suffix = path.suffix.lower()

    if suffix not in SUPPORTED_EXTENSIONS and suffix != ".htm":
        raise ValueError(f"Unsupported file type: {suffix}")

    return LOADERS[suffix](path)