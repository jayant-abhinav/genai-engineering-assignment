# Gemini LLM client.
import time
import logging
from google import genai
from google.genai import types
from problem2_llm_judge.core.config import Settings
from problem2_llm_judge.exceptions import LLMGenerationError

logger = logging.getLogger(__name__)
class GeminiLLM:

    # Wrapper around the Gemini API.
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def generate_json(self, prompt: str, response_schema: dict,) -> str:

        # Generate a structured JSON response using Gemini.
        logger.info(
            "Sending structured request to Gemini model '%s'.",
            self._settings.GEMINI_MODEL,
        )
        start_time = time.perf_counter()

        try:
            response = self._client.models.generate_content(
                model=self._settings.GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=self._settings.TEMPERATURE,
                    response_mime_type="application/json",
                    response_json_schema=response_schema,
                ),
            )

            elapsed_ms = (time.perf_counter() - start_time) * 1000
            logger.info(
                "Gemini request completed successfully | model=%s | latency=%.2f ms",
                self._settings.GEMINI_MODEL,
                elapsed_ms,
            )

            return response.text

        except Exception as exc:
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            logger.exception(
                "Gemini request failed | model=%s | latency=%.2f ms",
                self._settings.GEMINI_MODEL,
                elapsed_ms,
            )

            raise LLMGenerationError(
                "Failed to generate response from Gemini."
            ) from exc

    