# Week 3: LLM Observability and Usage Logging

## Objective
Implement usage tracking for Gemini API requests by measuring response latency, input and output token counts, calculating estimated cost, and saving each call log to MongoDB Atlas.

---

## What I Learnt
- How to measure response latency using Python's time.perf_counter().
- How to extract token counts from Gemini's usage_metadata (prompt_token_count and candidates_token_count).
- How to calculate estimated API cost using standard pricing ($0.30 per 1M input tokens, $2.50 per 1M output tokens).
- How to store records in MongoDB Atlas using PyMongo with automatic retries.
- How to build a safe fallback to save logs locally in api_usage_logs.json if network access or port 27017 is blocked.

---

## Files
- usage_logger.py: Connects to MongoDB Atlas and logs call data, with local JSON fallback.
- llm_client.py: Calls the model, calculates latency, tokens, cost, and sends data to the logger.
- main.py: CLI to run queries and view latency and token stats in real time.
- test_client.py: Unit tests verifying that the client logs usage properly using mock objects.
- requirements.txt: Package dependencies.
- .env: Stores GEMINI_API_KEY and MONGODB_URI.

---

## How to Run

### 1. Main Program
cd "Week 3"
python main.py

Press Enter to select Gemini, then type your question. The terminal displays latency in milliseconds, token counts, estimated cost in USD, and Gemini's response.

### 2. Unit Tests
python test_client.py
