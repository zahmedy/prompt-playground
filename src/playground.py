import argparse

from src.config import DEFAULT_MODEL, REASONING_FILE
from src.evaluator import evaluate_answer
from src.llm_client import ask
from src.utils import build_few_shot_prompt, load_examples


def run_reasoning_task(task: str) -> str:
    """Generate a reasoning answer using the few-shot examples."""
    examples = load_examples(REASONING_FILE)
    prompt = build_few_shot_prompt(task, examples)
    return ask(prompt=prompt, model=DEFAULT_MODEL)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prompt Engineering Playground demo runner"
    )
    parser.add_argument(
        "--task",
        type=str,
        default="What are three creative uses for a paperclip?",
        help="Task for the reasoning prompt",
    )
    parser.add_argument(
        "--evaluate",
        action="store_true",
        help="If set, also request an LLM-based evaluation of the answer.",
    )
    args = parser.parse_args()

    answer = run_reasoning_task(args.task)
    print("### Model answer ###\n")
    print(answer)

    if args.evaluate:
        print("\n### Evaluation ###\n")
        print(evaluate_answer(answer, model=DEFAULT_MODEL))


if __name__ == "__main__":
    main()
