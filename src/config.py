

import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = BASE_DIR / "prompts"
EXAMPLES_DIR = PROMPTS_DIR / "examples"

# Example file names
REASONING_FILE = EXAMPLES_DIR / "reasoning_fewshot.txt"
CLASSIFICATION_FILE = EXAMPLES_DIR / "classification_fewshot.txt"
CODING_FILE = EXAMPLES_DIR / "coding_fewshot.txt"

# Model defaults (can be overridden via environment)
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
DEFAULT_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.2"))
DEFAULT_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "300"))
