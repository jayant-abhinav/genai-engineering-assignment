from dataclasses import dataclass
from typing import Dict

@dataclass
class DocumentChunk:

    # Represents a chunk generated from a source document.
    chunk_id: str
    document_id: str
    source: str
    text: str
    chunk_index: int
    metadata: Dict