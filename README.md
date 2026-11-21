# Generative AI Laboratory Curriculum (Trimester 5)

Comprehensive practical implementation of Generative AI engineering concepts: from initial LLM API calls and provider-agnostic abstractions, to usage telemetry with MongoDB, multilingual tokenization analysis, token economics capacity planning, and golden set model benchmarking.

---

## 📚 Curriculum Overview

| Week | Module / Experiment | Core Technologies | Primary Focus |
| :--- | :--- | :--- | :--- |
| **[Week 1](./Week%201/README.md)** | **First LLM API Call** | Python 3.14, `google-genai`, `dotenv` | Authenticating with Google Gemini API securely using `.env` and generating completions. |
| **[Week 2](./Week%202/README.md)** | **Provider-Agnostic LLM Client** | Python ABC, Gemini API, Ollama, Pytest | Building a decoupled multi-provider abstraction (`LLMProvider`) with unit tests and Colab practical. |
| **[Week 3](./Week%203/README.md)** | **LLM Observability & Telemetry** | MongoDB Atlas, PyMongo, Gemini API | Tracking latency (ms), token volume, and dollar cost with resilient cloud and local fallback logging. |
| **[Week 4](./Week%204/README.md)** | **Tokenizer Architecture Comparison** | Hugging Face Transformers, SentencePiece | Comparing BPE, WordPiece, and SentencePiece across English, Telugu, and Hindi to analyze tokenization tax. |
| **[Week 5](./Week%205/README.md)** | **Token Economics & Budget Planning** | Python Dataclasses, Pytest | Estimating daily/monthly token expenditure and performing RPM/TPM concurrency and safety margin checks. |
| **[Week 6](./Week%206/README.md)** | **Systematic Model Evaluation** | Golden Question Dataset, Gemini API | Automated keyword coverage benchmarking (`PASS`/`REVIEW`) and release tracking in CSV format. |

---

## ⚡ Quick Start: Running Any Lab

### 1. Activate Environment (PowerShell)
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 2. Execution Quick Reference

```powershell
# Week 1: First LLM Call
cd "Week 1"; python main.py; cd ..

# Week 2: Provider-Agnostic Client & Tests
cd "Week 2"; python main.py; python test_client.py; cd ..

# Week 3: Observability & MongoDB Telemetry
cd "Week 3"; python main.py; python test_client.py; cd ..

# Week 4: Tokenizer Comparison (English, Telugu, Hindi)
cd "Week 4"; python tokenizer_comparison.py; cd ..

# Week 5: Token Economics & Budget Report
cd "Week 5"; python budget.py; python test_budget.py; cd ..

# Week 6: Golden Set Model Evaluation
cd "Week 6"; python main.py; cd ..
```
