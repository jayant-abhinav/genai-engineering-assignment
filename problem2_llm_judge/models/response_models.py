# Response models for the LLM Judge API.
from pydantic import BaseModel, Field

class EvaluationResult(BaseModel):
    
    #  Individual evaluation criterion.
    score: float = Field(
        ...,
        ge=0.0,
        le=10.0,
        description="Score for the evaluation criterion.",
    )

    feedback: str = Field(
        ...,
        description="Explanation of the assigned score.",
    )


class JudgeResponse(BaseModel):

    # Response returned by the judge.
    relevance: EvaluationResult
    correctness: EvaluationResult
    clarity: EvaluationResult

    overall_score: float = Field(
        ...,
        ge=0.0,
        le=10.0,
    )
    summary: str