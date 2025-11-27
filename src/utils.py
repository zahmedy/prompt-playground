import os
from pathlib import Path
from typing import Union

PathLike = Union[str, Path]


def load_examples(path: PathLike) -> str:
    """Load few-shot examples from a text file."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Examples file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_few_shot_prompt(task: str, examples: str) -> str:
    """Attach examples above the task."""
    return f"{examples}\n\nTask:\n{task}"
