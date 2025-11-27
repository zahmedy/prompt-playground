import os
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

from src.config import DEFAULT_MAX_TOKENS, DEFAULT_MODEL, DEFAULT_TEMPERATURE

load_dotenv()


def _get_client() -> OpenAI:
    """Return an OpenAI client, raising a clear error when the API key is missing."""
    api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Create a .env (see .env.example) or export it in your shell."
        )
    return OpenAI(api_key=api_key)


client = _get_client()


def ask(
    prompt: str = "Ask away!",
    model: str = DEFAULT_MODEL,
    temp: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
):
    """Send a prompt to the model and return the text response."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temp,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content
