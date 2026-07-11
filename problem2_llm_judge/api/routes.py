from fastapi import APIRouter, Depends
from problem2_llm_judge.core.dependencies import get_judge_service
from problem2_llm_judge.models.request_models import JudgeRequest
from problem2_llm_judge.services.judge_service import JudgeService
from problem2_llm_judge.models.response_models import JudgeResponse

router = APIRouter()

@router.post(
    "/judge",
    response_model=JudgeResponse,
    summary="Evaluate an LLM response",
    description="Evaluates an answer using the Gemini-based judge.",
    tags=["Judge"],
)

def judge(request: JudgeRequest, service: JudgeService = Depends(get_judge_service),):
    
    # Evaluate an answer using the judge service.
    result = service.evaluate(
        request.question,
        request.answer,
    )
    return service.evaluate(request.question, request.answer,)