from fastapi.testclient import TestClient
from unittest.mock import Mock
from problem2_llm_judge.core.dependencies import get_judge_service
from problem2_llm_judge.main import app
from problem2_llm_judge.models.response_models import (
    EvaluationResult,
    JudgeResponse,
)

def override_judge_service():
    service = Mock()
    service.evaluate.return_value = JudgeResponse(
        relevance=EvaluationResult(
            score=9,
            feedback="Relevant",
        ),
        correctness=EvaluationResult(
            score=10,
            feedback="Correct",
        ),
        clarity=EvaluationResult(
            score=8,
            feedback="Clear",
        ),
        overall_score=9,
        summary="Good answer",
    )
    return service

app.dependency_overrides[get_judge_service] = override_judge_service
client = TestClient(app)

def test_judge_endpoint():
    response = client.post(
        "/judge",
        json={
            "question": "What is AI?",
            "answer": "Artificial Intelligence",
        },
    )

    assert response.status_code == 200
    body = response.json()

    assert body["overall_score"] == 9
    assert body["correctness"]["score"] == 10

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"