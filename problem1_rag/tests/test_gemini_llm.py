from problem1_rag.app.llm.gemini_llm import GeminiLLM

def test_constructor():
    llm = GeminiLLM(api_key="dummy")

    assert llm.model_name