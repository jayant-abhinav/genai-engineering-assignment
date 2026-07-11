# Judge service
from problem2_llm_judge.services.gemini_llm import GeminiLLM

class JudgeService:

    # Service responsible for evaluating LLM responses.
    def __init__(self, llm: GeminiLLM) -> None:
        self._llm = llm

    def evaluate(self, question: str, answer: str) -> str:

        # Evaluate an answer using Gemini.
        prompt = f"""
                    You are an expert evaluator.

                    Question:
                    {question}

                    Answer:
                    {answer}

                    Provide your evaluation.
                """
        return self._llm.generate(prompt)