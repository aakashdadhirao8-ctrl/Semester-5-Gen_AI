import os
from pathlib import Path
from dotenv import load_dotenv
from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)

load_dotenv(Path(__file__).with_name(".env"))
load_dotenv(override=True)

provider_input = input(
    "Choose provider (gemini/ollama) [Default: gemini]: "
).strip().lower()

if provider_input in ["gemini", "1", ""]:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Gemini API key not found in .env")
    provider = GeminiProvider(api_key)
elif provider_input in ["ollama", "2"]:
    provider = OllamaProvider("llama3.2")
else:
    raise ValueError("Invalid provider selected. Please choose 'gemini' or 'ollama'.")

client = LLMClient(provider)
prompt = input("Enter your question: ")
answer = client.generate(prompt)

print("\nLLM Response:")
print(answer)
