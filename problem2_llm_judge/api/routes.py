# API routes for Problem 2.
from fastapi import APIRouter
from problem2_llm_judge.models.request_models import JudgeRequest
from problem2_llm_judge.models.response_models import (
    EvaluationResult,
    JudgeResponse,
)

router = APIRouter()

@router.post(
    "/judge",
    response_model=JudgeResponse,
    tags=["Judge"],
)
def judge(_: JudgeRequest) -> JudgeResponse:
    """
    Placeholder implementation.
    The JudgeService will replace this implementation
    in the next step.
    """

    return JudgeResponse(
        relevance=EvaluationResult(
            score=10,
            feedback="Placeholder",
        ),
        correctness=EvaluationResult(
            score=10,
            feedback="Placeholder",
        ),
        clarity=EvaluationResult(
            score=10,
            feedback="Placeholder",
        ),
        overall_score=10,
        summary="Judge service not implemented yet.",
    )