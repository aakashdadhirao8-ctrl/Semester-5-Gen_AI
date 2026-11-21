# Week 1: First LLM API Call

## 🎯 Lab Focus
Connect a Python application to a Large Language Model (LLM) using the Google Gemini API, authenticate securely using environment variables, and process AI-generated completions.

---

## 🧠 What We Have Learnt

1. **Role of API Keys in LLM Applications**:
   - Understand how API keys act as credentials to authenticate client applications, monitor usage, and apply billing/rate limits.
2. **Environment Variable Security**:
   - Learned why hardcoding secrets directly in source code is a major security risk.
   - Used `python-dotenv` and `.env` files to keep API keys secure and ignored by version control (`.gitignore`).
3. **Google GenAI SDK Integration**:
   - Initialized and used the official `google-genai` client library (`genai.Client`).
   - Dispatched structured generation requests using `client.models.generate_content`.
4. **Model Selection & Error Handling**:
   - Configured modern model endpoints (`gemini-3.8-flash`).
   - Diagnosed and resolved authentication (`API_KEY_INVALID`), model deprecation, and configuration errors.

---

## 📂 Project Structure

```text
Week 1/
├── .env                  # Secret API key (ignored by Git)
├── .env.example          # Template for environment configuration
├── .gitignore            # Excludes .env, .venv, and cache files
├── main.py               # Main application script
├── README.md             # Lab documentation and instructions
└── requirements.txt      # Python dependencies
```

---

## 🚀 How to Execute

### 1. Prerequisites & Environment Setup
Make sure your virtual environment is active in the terminal:
```powershell
# From the project root
.\.venv\Scripts\Activate.ps1
```

### 2. Configure Credentials
Ensure your `Week 1/.env` file contains your valid Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Run the Program
```powershell
cd "Week 1"
python main.py
```

### 4. Expected Output
```text
LLM Response:
At its simplest, Artificial Intelligence (AI) is about teaching machines to think, learn, and make decisions like humans...
```
*(To return to the root folder after running: `cd ..`)*
