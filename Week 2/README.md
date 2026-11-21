# Week 2: Provider-Agnostic LLM Client

## Objective
Build a provider-agnostic LLM client using an abstract base class so that the main application can switch between Gemini (cloud) and Ollama (local) without changing the core business logic.

---

## What I Learnt
- How to use Python's abc module (ABC, @abstractmethod) to create a common LLMProvider interface.
- How to implement concrete providers (GeminiProvider for cloud, OllamaProvider for local models).
- How to write automated unit tests using a FakeProvider to test client behavior without making live API calls.
- How to log request tokens, latency, and estimated cost in MongoDB Atlas.

---

## Files
- llm_client.py: Contains LLMProvider interface, GeminiProvider, OllamaProvider, and LLMClient.
- main.py: Interactive command line program to select provider and query the model.
- test_client.py: Unit tests verifying that LLMClient forwards prompts and receives responses.
- Week2_Gemini_MongoDB_Logging.ipynb: Jupyter/Colab notebook covering the complete 24-step MongoDB logging practical.
- requirements.txt: Python dependencies.
- .env: Stores GEMINI_API_KEY.

---

## How to Run

### Interactive Client
cd "Week 2"
python main.py

Press Enter at the prompt to default to Gemini, then enter your question.

### Unit Tests
python test_client.py

### Practical Notebook
Open Week2_Gemini_MongoDB_Logging.ipynb in VS Code or Google Colab to run the step-by-step MongoDB usage logging practical.
