# Week 2: Provider-Agnostic LLM Client

## Objective
Build a provider-agnostic LLM client using an abstract base class so that the main application can switch between Gemini (cloud) and Ollama (local) without changing the core business logic.

## What I Learnt
- How to use Python's `abc` module (`ABC`, `@abstractmethod`) to define a common interface (`LLMProvider`).
- How to write provider implementations (`GeminiProvider` for cloud API, `OllamaProvider` for local models).
- How to write unit tests using a `FakeProvider` to test the client logic without making live or paid API calls.
- How to track tokens, latency, and estimated cost in MongoDB through the accompanying Colab notebook (`Week2_Gemini_MongoDB_Logging.ipynb`).

## Files
- `llm_client.py`: Defines the `LLMProvider` interface, `GeminiProvider`, `OllamaProvider`, and `LLMClient`.
- `main.py`: Interactive CLI to select provider and query the model.
- `test_client.py`: Unit test verifying that `LLMClient` correctly forwards prompts and returns answers.
- `Week2_Gemini_MongoDB_Logging.ipynb`: Jupyter notebook covering the complete 24-step Gemini and MongoDB logging practical.
- `requirements.txt`: Python package requirements.
- `.env`: Contains `GEMINI_API_KEY`.

## How to Run

### 1. Interactive Client
```powershell
cd "Week 2"
python main.py
```
- At the prompt `Choose provider (gemini/ollama) [Default: gemini]:`, press `Enter`.
- Enter your question (e.g., `What is Generative AI?`).

### 2. Unit Tests
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

### 3. Practical Notebook
Open `Week2_Gemini_MongoDB_Logging.ipynb` in VS Code or Google Colab to run the step-by-step MongoDB usage logging practical.
