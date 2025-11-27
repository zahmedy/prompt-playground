from src.llm_client import ask

RUBRIC = """
Evaluate the answer using this rubric:
- Correctness (0-5)
- Reasoning clarity (0-5)
- Conciseness (0-5)
Provide a final score out of 15 and short feedback.
"""

def evaluate_answer(answer, model="gpt-4o-mini"):
    """Grade an answer using the rubric"""
    prompt = f"{RUBRIC}\n\nAnswer:\n{answer}"
    return ask(prompt, model=model)

