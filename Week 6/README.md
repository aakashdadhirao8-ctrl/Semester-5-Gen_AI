# Week 6: Model Evaluation with Golden Dataset

## Objective
Evaluate model answers against a 30-question golden question set using keyword-based coverage scoring, categorize results into PASS or REVIEW, and export the baseline run to CSV.

---

## What I Learnt
- How to create and structure a golden evaluation dataset with expected answers, target keywords, and references.
- How to measure response accuracy using keyword recall:
  Score = (Matched Keywords / Total Keywords) * 100
- How to apply classification thresholds:
  PASS: Coverage 60% or higher
  REVIEW: Coverage below 60%
  ERROR: Request failure or timeout
- How to export benchmark results to CSV (baseline_results.csv) with version tracking (v0.1) to measure model changes over time.

---

## Files
- golden_set.json: 30 curated questions on LLMs, tokenization, and architecture with expected keywords.
- main.py: Evaluation runner supporting Gemini API, Ollama, and quick summary viewing.
- baseline_results.csv: Saved evaluation records containing questions, answers, keyword matches, and scores.
- requirements.txt: Package dependencies.
- .env: Stores GEMINI_API_KEY.

---

## How to Run

cd "Week 6"
python main.py

---

## Available Options

Option 3: Quick Summary
Type 3 and press Enter. It reads the existing baseline_results.csv and prints the total questions evaluated, pass count, review count, and average keyword coverage percentage.

Option 1: Live Evaluation with Gemini
Press Enter to select Gemini gemini-3.8-flash, enter the number of questions to test (e.g. 5 for a quick demo, or all for all 30), and the script will query the model, score each question, and update baseline_results.csv.
