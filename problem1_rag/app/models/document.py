from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

@dataclass(slots=True)
class Document:
    
    # Represents a document after ingestion.
    source: Path
    file_type: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)