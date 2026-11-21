# Generative AI Lab - Semester 5

This repository contains my weekly laboratory implementations for the Generative AI course.

## Weekly Overview

- **Week 1: First LLM API Call**  
  Connecting to Google Gemini API using Python, managing API keys securely with `.env`, and generating text responses.

- **Week 2: Provider-Agnostic LLM Client**  
  Building an abstract interface over both cloud (Gemini) and local (Ollama) models, with unit tests and MongoDB logging.

- **Week 3: LLM Observability and Logging**  
  Measuring latency, token counts, and estimated cost for each query, with logging to MongoDB Atlas and local fallback.

- **Week 4: Tokenizer Comparison**  
  Comparing BPE (GPT-2), WordPiece (BERT), and SentencePiece (XLM-R) tokenization across English, Telugu, and Hindi.

- **Week 5: Token Economics and Budget Planning**  
  Calculating daily and monthly token consumption, cost estimates, and checking RPM/TPM limits with safety margins.

- **Week 6: Model Evaluation with Golden Dataset**  
  Evaluating model outputs against a 30-question golden dataset using keyword matching and saving results to CSV.

---

## Environment Setup

To run any of the labs, activate the virtual environment first:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Install requirements if not already installed:

```powershell
pip install google-genai python-dotenv requests pymongo dnspython pytest
```

---

## Execution Commands

- **Week 1**: `cd "Week 1"; python main.py; cd ..`
- **Week 2**: `cd "Week 2"; python main.py; python test_client.py; cd ..`
- **Week 3**: `cd "Week 3"; python main.py; python test_client.py; cd ..`
- **Week 4**: `cd "Week 4"; python tokenizer_comparison.py; cd ..`
- **Week 5**: `cd "Week 5"; python budget.py; python test_budget.py; cd ..`
- **Week 6**: `cd "Week 6"; python main.py; cd ..`
