import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Step 1: Load API key from .env (checks local directory and current working directory)
load_dotenv(Path(__file__).with_name(".env"))
load_dotenv()

# Step 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found! Check that .env exists in the Week 1 directory "
        "and contains GEMINI_API_KEY=your_key."
    )

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Make first LLM API call
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Step 5: Display response
print("\nLLM Response:")
print(response.text)
