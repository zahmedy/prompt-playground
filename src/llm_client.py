import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask(prompt="Ask Away!", model="gpt-40-mini", temp=0.2, max_tokens=300):
    """
    Send a ptompt to the model and return the output
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temp,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content