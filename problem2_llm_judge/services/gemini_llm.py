# Gemini LLM client
import logging
from google import genai
from problem2_llm_judge.core.config import Settings

logger = logging.getLogger(__name__)

class GeminiLLM:
    
    # Wrapper around the Gemini API.
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def generate(self, prompt: str) -> str:
        
        # Generate a response from Gemini.
        logger.info("Sending request to Gemini model '%s'.", self._settings.GEMINI_MODEL)

        response = self._client.models.generate_content(
            model=self._settings.GEMINI_MODEL,
            contents=prompt,
        )

        text = response.text.strip()
        logger.info("Received response from Gemini.")

        return text