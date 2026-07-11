# Request models for the LLM Judge API.
from pydantic import BaseModel, Field

class JudgeRequest(BaseModel):
 
    # Request payload for evaluating an LLM response.
    question: str = Field(
        ...,
        min_length=1,
        description="The user's original question.",
    )

    answer: str = Field(
        ...,
        min_length=1,
        description="The LLM-generated answer to evaluate.",
    )