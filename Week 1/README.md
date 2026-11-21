# Week 1: First LLM API Call

## Objective
Connect a Python script to an LLM using the Google Gemini API, store the API key securely in a .env file, and print the generated response.

---

## What I Learnt
- Why an API key is required to authenticate client programs with an LLM platform.
- How to store keys securely in a .env file instead of hardcoding them in the script.
- How to load environment variables using python-dotenv.
- How to initialize the google-genai client and request a completion with gemini-3.8-flash.
- How to recognize and resolve common errors such as invalid API keys and missing dependencies.

---

## Files
- main.py: Python script to load the key, call Gemini, and print the response.
- .env: Stores the secret GEMINI_API_KEY.
- .env.example: Example template showing how to set up the .env file.
- requirements.txt: List of required Python packages.
- .gitignore: Prevents .env and virtual environment files from being pushed to Git.

---

## How to Run

1. Open terminal in the Week 1 folder:
cd "Week 1"

2. Make sure your .env file has your key:
GEMINI_API_KEY=your_key_here

3. Run the script:
python main.py

---

## Expected Output
The script prints the heading followed by Gemini's explanation of Artificial Intelligence in simple words.
