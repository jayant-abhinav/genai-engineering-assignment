from unittest.mock import MagicMock, patch
import pytest
from problem2_llm_judge.core.config import Settings
from problem2_llm_judge.exceptions import LLMGenerationError
from problem2_llm_judge.services.gemini_llm import GeminiLLM

@patch("problem2_llm_judge.services.gemini_llm.genai.Client")
def test_generate_json_success(mock_client):
    # Test successful JSON generation.
    response = MagicMock()
    response.text = '{"status":"ok"}'

    client = MagicMock()
    client.models.generate_content.return_value = response

    mock_client.return_value = client
    settings = Settings(GEMINI_API_KEY="dummy")
    llm = GeminiLLM(settings)

    result = llm.generate_json(
        prompt="Hello",
        response_schema={},
    )

    assert result == '{"status":"ok"}'
    client.models.generate_content.assert_called_once()


@patch("problem2_llm_judge.services.gemini_llm.genai.Client")
def test_generate_json_failure(mock_client):
    # Test Gemini exception handling.

    client = MagicMock()
    client.models.generate_content.side_effect = Exception(
        "API Failure"
    )

    mock_client.return_value = client
    settings = Settings(GEMINI_API_KEY="dummy")
    llm = GeminiLLM(settings)

    with pytest.raises(LLMGenerationError):
        llm.generate_json(
            prompt="Hello",
            response_schema={},
        )