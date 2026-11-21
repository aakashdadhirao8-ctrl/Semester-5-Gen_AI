# Week 1: First LLM API Call

## Objective
The objective of this lab is to connect a Python script to an LLM using the Google Gemini API, store the API key securely in a `.env` file, and print the generated response.

## What I Learnt
- Why API keys are required to authenticate client programs with an LLM platform.
- How to store keys securely in a `.env` file instead of hardcoding them in the script.
- How to load environment variables using `python-dotenv`.
- How to initialize the `google-genai` client and make a request with `gemini-3.8-flash`.
- How to handle common setup issues like invalid API keys and missing dependencies.

## Files
- `main.py`: Python code to load the key, call Gemini, and print the response.
- `.env`: Contains the secret `GEMINI_API_KEY` (kept out of Git).
- `.env.example`: Example file showing how to structure the `.env` file.
- `requirements.txt`: Required Python packages.
- `.gitignore`: Prevents `.env` and `.venv` from being pushed to GitHub.

## How to Run

1. Make sure your `.venv` is activated.
2. Ensure `Week 1/.env` contains your API key:
   ```env
   GEMINI_API_KEY=your_actual_key
   ```
3. Run the script:
   ```powershell
   cd "Week 1"
   python main.py
   ```

## Expected Output
```text
LLM Response:
At its simplest, Artificial Intelligence (AI) is about teaching machines to think, learn, and make decisions like humans...
```
