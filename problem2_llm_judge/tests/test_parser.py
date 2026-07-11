import pytest
from problem2_llm_judge.exceptions import (
    ResponseParsingError,
    ResponseValidationError,
)
from problem2_llm_judge.services.parser import JsonParser

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

def test_parse_valid_json():
    result = JsonParser.parse(VALID_RESPONSE)

    assert result.overall_score == 9
    assert result.relevance.score == 9
    assert result.correctness.score == 10

def test_parse_markdown_json():
    response = f"```json\n{VALID_RESPONSE}\n```"
    result = JsonParser.parse(response)

    assert result.summary == "Good answer"

def test_invalid_json():
    with pytest.raises(ResponseParsingError):
        JsonParser.parse("not json")

def test_invalid_schema():
    invalid = '{"hello":"world"}'
    with pytest.raises(ResponseValidationError):
        JsonParser.parse(invalid)