# Week 6: Model Evaluation with Golden Dataset

## Objective
Evaluate model answers against a 30-question golden question set using keyword-based coverage scoring, categorize results into PASS or REVIEW, and export the baseline run to CSV.

## What I Learnt
- How to create and structure a golden evaluation dataset with expected answers, target keywords, and references.
- How to measure response accuracy using keyword recall:
  - Score = (Matched Keywords / Total Keywords) * 100
- How to apply classification thresholds:
  - PASS: Coverage >= 60%
  - REVIEW: Coverage < 60%
  - ERROR: Request failure or timeout
- How to export benchmark results to CSV (`baseline_results.csv`) with version tracking (`v0.1`) to measure model regression over time.

## Files
- `golden_set.json`: 30 curated questions on LLMs, tokenization, and architecture with expected keywords.
- `main.py`: Evaluation runner supporting Gemini API, Ollama, and quick summary viewing.
- `baseline_results.csv`: Saved evaluation records containing questions, answers, keyword matches, and scores.
- `requirements.txt`: Package dependencies (`requests`, `google-genai`, `python-dotenv`).
- `.env`: Holds `GEMINI_API_KEY`.

## How to Run

```powershell
cd "Week 6"
python main.py
```

### Options:

1. **Option 3 (Quick Summary - Instant)**:
   - Type `3` and press `Enter`.
   - Reads the existing `baseline_results.csv` and prints the evaluation summary:
     ```text
     ======================================
     BASELINE EVALUATION SUMMARY (From CSV)
     ======================================
     Release Version: v0.1
     Total Questions Evaluated: 30
     Passed Questions (>=60%): 15
     Questions for Review (<60%): 14
     Failed / Error Requests: 1
     Average Keyword Coverage: 57.50%
     ```

2. **Option 1 (Live Evaluation with Gemini)**:
   - Press `Enter` (defaults to Gemini `gemini-3.8-flash`).
   - Enter number of questions (e.g. `5` for a quick demo, or `all` for all 30).
   - The script queries the model, calculates scores in real time, and updates `baseline_results.csv`.
