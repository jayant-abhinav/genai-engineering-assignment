from abc import ABC, abstractmethod

class LLMService(ABC):

    # Abstract interface for all LLM providers.
    @abstractmethod
    def generate(self, prompt: str) -> str:

        # Generate a response from the LLM.
        pass