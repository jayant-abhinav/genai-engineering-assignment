from google import genai
from google.genai.errors import (
    ClientError,
    ServerError,
)
from tenacity import (
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)
from problem1_rag.app.llm.llm_service import LLMService
from problem1_rag.app.core.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    LLM_MAX_RETRIES,
    LLM_RETRY_MIN_WAIT,
    LLM_RETRY_MAX_WAIT,
)

def should_retry(exception: Exception) -> bool:

    # Retry only transient Gemini API errors.
    if isinstance(exception, ServerError):
        return True

    if isinstance(exception, ClientError):
        return exception.status_code == 429

    return False

class GeminiLLM(LLMService):

    # Google Gemini implementation.
    def __init__(self,api_key: str, model_name: str = GEMINI_MODEL,):
        if not api_key:
            raise ValueError("Gemini API key is required.")

        self.model_name = model_name
        self.client = genai.Client(api_key=api_key)

    @retry(
        retry=retry_if_exception(should_retry),
        stop=stop_after_attempt(LLM_MAX_RETRIES),
        wait=wait_exponential(
            multiplier=1,
            min=LLM_RETRY_MIN_WAIT,
            max=LLM_RETRY_MAX_WAIT,
        ),
        reraise=True,
    )

    def _generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )

        return response.text

    def generate(self, prompt: str) -> str:

        # Generate a response using Gemini.
        return self._generate(prompt)