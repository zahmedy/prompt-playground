import os
from pathlib import Path
from typing import Union
import json

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

def build_chain_of_thought(task):
    return f"{task}\n\nThink step by step and show reasoning."

def build_socratic_style(task):
    return f"You are a Socratic tutor. Ask guided questions.\n\n{task}"

def try_parse_json(text):
    """JSON Parsing util"""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


