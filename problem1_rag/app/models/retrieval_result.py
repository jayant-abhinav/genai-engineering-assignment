from dataclasses import dataclass

@dataclass(slots=True)
class RetrievalResult:

    # Represents a retrieved document chunk.
    text: str
    source: str
    file_type: str
    chunk_index: int
    distance: float