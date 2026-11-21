# Week 2: Provider-Agnostic LLM Client & Observability Practical

## 🎯 Lab Focus
Design and implement a provider-agnostic LLM interface in Python that decouples your application logic from any single LLM vendor (supporting hosted cloud APIs like Gemini and local models like Ollama), with automated unit testing and a comprehensive token-logging practical.

---

## 🧠 What We Have Learnt

1. **Design Patterns in GenAI Architecture**:
   - Implemented the **Strategy / Factory Pattern** using Python's `abc` module (`ABC`, `@abstractmethod`).
   - Created a uniform `LLMProvider` contract with a single `.generate(prompt)` signature.
2. **Pluggable Multi-Provider Support**:
   - **`GeminiProvider`**: Communicates with Google AI cloud services over HTTPS.
   - **`OllamaProvider`**: Communicates with local self-hosted open-weights models (`llama3.2` / `qwen2.5-coder`) over HTTP REST endpoints (`http://localhost:11434/api/generate`).
3. **Automated Unit Testing with Mocks**:
   - Built mock providers (`FakeProvider`) to test consumer code (`LLMClient`) deterministically and for free, without making external network calls or incurring API costs.
4. **Usage Observability Practical (`Week2_Gemini_MongoDB_Logging.ipynb`)**:
   - Token counting (`prompt_token_count`, `candidates_token_count`, `total_token_count`).
   - Measuring response latency using `time.perf_counter()`.
   - Applying pricing models ($0.30/1M input, $2.50/1M output).
   - Implementing exponential backoff retries with random jitter for transient errors.
   - Upserting telemetry documents to MongoDB Atlas and visualizing with Pandas and Matplotlib.

---

## 📂 Project Structure

```text
Week 2/
├── .env                                  # Secret credentials (ignored by Git)
├── .env.example                          # Environment variable template
├── .gitignore                            # Ignores secrets and Python cache
├── llm_client.py                         # Abstract LLMProvider, Gemini & Ollama implementations
├── main.py                               # Interactive CLI selecting provider and running queries
├── README.md                             # Documentation and usage guide
├── requirements.txt                      # Dependencies (google-genai, requests, pytest)
├── test_client.py                        # Unit tests using FakeProvider
└── Week2_Gemini_MongoDB_Logging.ipynb   # Complete 24-step Google Colab / Jupyter Practical
```

---

## 🚀 How to Execute

### 1. Run the Interactive Client (`main.py`)
```powershell
cd "Week 2"
python main.py
```
- **Provider Prompt**: Press `Enter` (or type `gemini`) to use Gemini AI.
- **Question Prompt**: Type any question (e.g. `What is a Large Language Model?`).
- **Expected Output**:
  ```text
  LLM Response:
  A Large Language Model (LLM) is an artificial intelligence model trained on vast amounts of text...
  ```

### 2. Run the Automated Unit Tests (`test_client.py`)
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

### 3. Run the Colab Practical (`Week2_Gemini_MongoDB_Logging.ipynb`)
- Open the `.ipynb` file in VS Code (with the Jupyter extension) or upload it to [Google Colab](https://colab.research.google.com/).
- Run the cells in order to execute the full 24-step pipeline including MongoDB logging, data tables, and Matplotlib latency/token/cost charts.

*(To return to the root folder after running: `cd ..`)*
