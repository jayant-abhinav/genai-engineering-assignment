# Dependency providers
from functools import lru_cache
from problem2_llm_judge.core.config import get_settings
from problem2_llm_judge.services.gemini_llm import GeminiLLM
from problem2_llm_judge.services.judge_service import JudgeService

@lru_cache
def get_llm() -> GeminiLLM:
    return GeminiLLM(get_settings())

@lru_cache
def get_judge_service() -> JudgeService:
    return JudgeService(
        llm=get_llm(),
        settings=get_settings(),
    )