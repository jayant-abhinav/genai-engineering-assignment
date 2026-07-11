# Judge service
import logging
from problem2_llm_judge.core.config import Settings
from problem2_llm_judge.exceptions import (
    LLMGenerationError,
    ResponseParsingError,
)
from problem2_llm_judge.models.response_models import (
    JUDGE_RESPONSE_SCHEMA,
    JudgeResponse,
)
from problem2_llm_judge.prompts.judge_prompt import JudgePromptBuilder
from problem2_llm_judge.services.gemini_llm import GeminiLLM
from problem2_llm_judge.services.parser import JsonParser

logger = logging.getLogger(__name__)

class JudgeService:

    # Service responsible for evaluating LLM responses.
    def __init__(self, llm: GeminiLLM, settings: Settings,) -> None:
        self._llm = llm
        self._settings = settings

    def evaluate(self, question: str, answer: str,) -> JudgeResponse:

        # Evaluate an answer using Gemini.
        logger.info("Starting evaluation.")
        prompt = JudgePromptBuilder.build(
            question=question,
            answer=answer,
        )

        last_exception: Exception | None = None
        for attempt in range(self._settings.MAX_RETRIES + 1):

            logger.info(
                "Evaluation attempt %s/%s",
                attempt + 1,
                self._settings.MAX_RETRIES + 1,
            )

            try:
                raw_response = self._llm.generate_json(
                    prompt=prompt,
                    response_schema=JUDGE_RESPONSE_SCHEMA,
                )

                result = JsonParser.parse(raw_response)
                logger.info("Evaluation completed successfully.")
                return result

            except (LLMGenerationError, ResponseParsingError) as exc:

                logger.warning(
                    "Evaluation attempt %s failed: %s",
                    attempt + 1,
                    exc,
                )

                last_exception = exc

        logger.error(
            "Evaluation failed after %s attempts.",
            self._settings.MAX_RETRIES + 1,
        )
        
        if last_exception is None:
            raise RuntimeError(
                "Evaluation failed without an exception."
            )
        raise last_exception