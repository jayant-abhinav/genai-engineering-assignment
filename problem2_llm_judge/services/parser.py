# Utilities for parsing Gemini responses.
import json
import logging
import re
from json import JSONDecodeError
from pydantic import ValidationError
from problem2_llm_judge.exceptions import (
    ResponseParsingError,
    ResponseValidationError,
)
from problem2_llm_judge.models.response_models import JudgeResponse

logger = logging.getLogger(__name__)

class JsonParser:

    # Parse and validate Gemini JSON responses.
    @staticmethod
    def parse(response_text: str) -> JudgeResponse:

        # Extract JSON from the LLM response and validate it.
        # Remove Markdown code fences if present
        cleaned = re.sub(r"```json|```", "", response_text).strip()

        # Extract JSON object
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)

        if not match:
            logger.error("No JSON object found in Gemini response.")
            raise ResponseParsingError(
                "No JSON object found in Gemini response."
            )

        try:
            data = json.loads(match.group(0))
        except JSONDecodeError as exc:
            logger.error("Invalid JSON returned by Gemini.")
            raise ResponseParsingError(
                "Invalid JSON returned by Gemini."
            ) from exc

        try:
            result = JudgeResponse.model_validate(data)
            logger.info("Successfully parsed Gemini response.")
            return result

        except ValidationError as exc:
            logger.error(
                "Gemini response does not match the expected schema."
            )

            raise ResponseValidationError(
                "Gemini response does not match the expected schema."
            ) from exc