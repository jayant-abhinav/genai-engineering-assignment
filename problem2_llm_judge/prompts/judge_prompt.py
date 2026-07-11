# Prompt builder for the LLM Judge.
class JudgePromptBuilder:

    @staticmethod
    def build(question: str, answer: str) -> str:
        return f"""
                    You are an expert AI evaluator.

                    Evaluate the answer using these criteria:
                    - Relevance
                    - Correctness
                    - Clarity

                    Score each criterion from 0 to 10.
                    Be objective and concise.

                    Question:
                    {question}

                    Answer:
                    {answer}
                """