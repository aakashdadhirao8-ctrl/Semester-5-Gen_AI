# Week 3: LLM Observability & Telemetry Logging with MongoDB

## 🎯 Lab Focus
Build a production-grade observability system that wraps an LLM client, intercepts every request/response cycle, measures latency in milliseconds, captures token counts, calculates estimated monetary cost, and persists the telemetry data in MongoDB Atlas with resilient fallback handling.

---

## 🧠 What We Have Learnt

1. **AI Application Telemetry**:
   - Why tracking usage metrics is critical for production GenAI applications (monitoring billing, detecting rate limit spikes, and debugging latency regressions).
2. **High-Resolution Latency Measurement**:
   - Used Python's `time.perf_counter()` to record end-to-end roundtrip latency in milliseconds with sub-millisecond precision.
3. **Dynamic Cost Estimation**:
   - Implemented real-time token cost estimation using provider-specific pricing tier formulas:
     $$\text{Cost (USD)} = \frac{\text{Input Tokens} \times \text{Input Price}}{1,000,000} + \frac{\text{Output Tokens} \times \text{Output Price}}{1,000,000}$$
4. **Resilient Database Logging & Fault Tolerance**:
   - Configured `pymongo.MongoClient` with timeouts and retry mechanisms.
   - Designed a **dual-destination logging strategy**: Attempts to save records to MongoDB Atlas cloud database; if blocked by institutional firewalls (e.g. port 27017) or network outages, it automatically falls back to local structured JSON logging (`api_usage_logs.json`) without interrupting user queries.

---

## 📂 Project Structure

```text
Week 3/
├── .env                  # Contains GEMINI_API_KEY and MONGODB_URI (ignored by Git)
├── .env.example          # Environment variable template
├── .gitignore            # Excludes secrets, logs, and cache
├── llm_client.py         # LLM client with latency, token, and cost tracking
├── main.py               # Application entrypoint
├── README.md             # Documentation and usage guide
├── requirements.txt      # Dependencies (pymongo, google-genai, requests, pytest)
├── test_client.py        # Unit tests using FakeProvider and FakeLogger
└── usage_logger.py       # Telemetry logger supporting MongoDB Atlas & local JSON fallback
```

---

## 🚀 How to Execute

### 1. Run the Application with Telemetry Logging
```powershell
cd "Week 3"
python main.py
```
- **Provider Prompt**: Press `Enter` (defaults to `gemini`).
- **Question Prompt**: Enter your question (e.g. `What is Machine Learning?`).
- **Expected Output**:
  ```text
  Usage details saved to MongoDB Atlas.  (or logged to api_usage_logs.json)
  Latency: 1120.45 ms
  Input tokens: 7
  Output tokens: 104
  Estimated cost (USD): 0.0002621

  LLM Response:
  Machine Learning is a subset of Artificial Intelligence that allows computers to learn from data...
  ```

### 2. Run the Unit Tests
```powershell
python test_client.py
```
- **Expected Output**:
  ```text
  .
  ----------------------------------------------------------------------
  Ran 1 test in 0.001s

  OK
  ```

*(To return to the root folder after running: `cd ..`)*
