from dataclasses import dataclass, field
from typing import Any
from pathlib import Path


@dataclass(slots=True)
class DocumentChunk:
    chunk_id: str
    source: Path
    file_type: str
    text: str
    chunk_index: int
    metadata: dict[str, Any] = field(default_factory=dict)