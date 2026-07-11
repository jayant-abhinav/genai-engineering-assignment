# Custom exceptions for LLM Judge.
class LLMJudgeError(Exception):
    """Base exception for the LLM Judge application."""

class LLMGenerationError(LLMJudgeError):
    """Raised when Gemini fails to generate a response."""

class ResponseParsingError(LLMJudgeError):
    """Raised when the LLM response cannot be parsed."""

class ResponseValidationError(LLMJudgeError):
    """Raised when the parsed response does not match the expected schema."""