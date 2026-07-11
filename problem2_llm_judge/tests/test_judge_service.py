import pytest
from unittest.mock import Mock
from problem2_llm_judge.core.config import Settings
from problem2_llm_judge.models.response_models import JUDGE_RESPONSE_SCHEMA
from problem2_llm_judge.services.gemini_llm import GeminiLLM
from problem2_llm_judge.services.judge_service import JudgeService
from problem2_llm_judge.exceptions import LLMGenerationError


VALID_RESPONSE = """
{
    "relevance":{
        "score":9,
        "feedback":"Relevant"
    },
    "correctness":{
        "score":10,
        "feedback":"Correct"
    },
    "clarity":{
        "score":8,
        "feedback":"Clear"
    },
    "overall_score":9,
    "summary":"Good answer"
}
"""

def test_judge_service_success():
    mock_llm = Mock(spec=GeminiLLM)
    mock_llm.generate_json.return_value = VALID_RESPONSE

    settings = Settings(
        GEMINI_API_KEY="dummy",
    )

    service = JudgeService(
        llm=mock_llm,
        settings=settings,
    )

    result = service.evaluate(
        "What is AI?",
        "Artificial Intelligence",
    )

    assert result.overall_score == 9
    assert result.correctness.score == 10

    mock_llm.generate_json.assert_called_once()

def test_judge_service_retry():
    mock_llm = Mock(spec=GeminiLLM)
    mock_llm.generate_json.side_effect = [
        LLMGenerationError("Temporary failure"),
        VALID_RESPONSE,
    ]

    settings = Settings(
        GEMINI_API_KEY="dummy",
        MAX_RETRIES=1,
    )

    service = JudgeService(
        llm=mock_llm,
        settings=settings,
    )

    result = service.evaluate(
        "Question",
        "Answer",
    )

    assert result.overall_score == 9
    assert mock_llm.generate_json.call_count == 2

def test_judge_service_retry_exhausted():
    mock_llm = Mock(spec=GeminiLLM)
    mock_llm.generate_json.side_effect = LLMGenerationError(
        "Gemini unavailable"
    )

    settings = Settings(
        GEMINI_API_KEY="dummy",
        MAX_RETRIES=2,
    )

    service = JudgeService(
        llm=mock_llm,
        settings=settings,
    )

    with pytest.raises(LLMGenerationError):
        service.evaluate(
            "Question",
            "Answer",
        )

    assert mock_llm.generate_json.call_count == 3