from problem2_llm_judge.prompts.judge_prompt import JudgePromptBuilder

def test_build_prompt_contains_question_and_answer():
    question = "What is AI?"
    answer = "Artificial Intelligence."

    prompt = JudgePromptBuilder.build(question, answer)

    assert question in prompt
    assert answer in prompt
    assert "Relevance" in prompt
    assert "Correctness" in prompt
    assert "Clarity" in prompt