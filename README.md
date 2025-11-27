# Prompt Playground

A lightweight prompt engineering playground with a few-shot workflow and an optional rubric-based self-evaluator. The repository is organized for quick experimentation while staying production-friendly for a portfolio.

## Features
- Few-shot prompt building using curated examples under `prompts/examples/`
- OpenAI chat client with centralized defaults and env-driven overrides
- Optional answer evaluator driven by a concise rubric
- Demo script for quick runs from the CLI

## Getting started
1. Create your environment file:
   ```bash
   cp .env.example .env
   # paste your OPENAI_API_KEY value inside .env
   ```
2. Install dependencies (ideally inside a virtualenv):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Run the demo reasoning flow (defaults to a simple creativity prompt):
  ```bash
  python -m src.playground
  ```
- Pass a custom task:
  ```bash
  python -m src.playground --task "Explain transformers like I'm five."
  ```
- Include an LLM-based evaluation of the answer:
  ```bash
  python -m src.playground --task "Explain transformers like I'm five." --evaluate
  ```

## Project layout
```
prompt-playground/
├── notebooks/
│   └── prompt_playground.ipynb
├── prompts/
│   ├── templates.yaml
│   └── examples/
├── data/
│   └── test_inputs.csv
├── src/
│   ├── config.py         # Paths and model defaults
│   ├── llm_client.py     # OpenAI client wrapper
│   ├── evaluator.py      # Rubric-based scoring
│   └── utils.py          # Helpers for loading examples/building prompts
└── README.md
```
