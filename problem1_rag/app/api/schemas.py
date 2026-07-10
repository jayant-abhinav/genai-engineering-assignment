from pydantic import BaseModel, Field

class AskRequest(BaseModel):

    # Request body for RAG question answering.
    question: str = Field(
        ...,
        min_length=1,
        description="User question",
    )

class SourceResponse(BaseModel):
    
    # Metadata about a retrieved source.
    source: str
    chunk_index: int


class AskResponse(BaseModel):
    
    # API response.
    answer: str
    sources: list[SourceResponse]