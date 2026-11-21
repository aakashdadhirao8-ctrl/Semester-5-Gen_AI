# Week 3: LLM Observability and Usage Logging

## Objective
Implement usage tracking for Gemini API requests by measuring response latency, input and output token counts, calculating estimated cost, and saving each call log to MongoDB Atlas.

## What I Learnt
- How to measure response latency using Python's `time.perf_counter()`.
- How to extract token counts from Gemini's `usage_metadata` (`prompt_token_count` and `candidates_token_count`).
- How to calculate estimated API cost using standard pricing ($0.30 per 1M input tokens, $2.50 per 1M output tokens).
- How to store records in MongoDB Atlas using PyMongo with retries.
- How to build a safe fallback to save logs locally in `api_usage_logs.json` if network access or port 27017 is blocked.

## Files
- `usage_logger.py`: Handles connecting to MongoDB Atlas and logging calls, with local JSON fallback.
- `llm_client.py`: Calls the model, calculates latency, tokens, cost, and passes data to the logger.
- `main.py`: CLI to run queries and view latency and token stats in real time.
- `test_client.py`: Unit test verifying that the client logs usage properly using mock objects.
- `requirements.txt`: Package dependencies (`pymongo`, `google-genai`, `requests`, `python-dotenv`, `pytest`).
- `.env`: Holds `GEMINI_API_KEY` and `MONGODB_URI`.

## How to Run

### 1. Run the Main Script
```powershell
cd "Week 3"
python main.py
```
- Press `Enter` to select `gemini`.
- Enter your question (e.g., `What is Machine Learning?`).

Expected output:
```text
Latency: 1145.23 ms
Input tokens: 7
Output tokens: 104
Estimated cost (USD): 0.0002621

LLM Response:
Machine Learning is a subset of Artificial Intelligence...
```

### 2. Run the Unit Test
```powershell
python test_client.py
```
Expected output:
```text
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```
