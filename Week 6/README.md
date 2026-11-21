# Week 6: Systematic Model Evaluation with Golden Dataset

## 🎯 Lab Focus
Design and execute a systematic evaluation pipeline for Large Language Models by comparing model responses against an annotated **Golden Question Set**, scoring answers using keyword-based coverage metrics, and exporting reproducible benchmark results to CSV.

---

## 🧠 What We Have Learnt

1. **Golden Dataset Creation & Annotation**:
   - Curated a structured 30-question benchmark dataset (`golden_set.json`) covering core LLM and tokenization concepts.
   - Annotated each question with verified reference answers, mandatory domain keywords, and citation sources.
2. **Automated Coverage Scoring Algorithm**:
   - Computed normalized keyword recall coverage for generated responses:
     $$\text{Coverage Score} = \left(\frac{\text{Number of Matched Keywords}}{\text{Total Expected Keywords}}\right) \times 100\%$$
3. **Threshold Classification Gates**:
   - Categorized each output into actionable release statuses:
     - **`PASS`**: Score $\ge 60\%$ (response captures the essential factual keywords).
     - **`REVIEW`**: Score $< 60\%$ (response missing core concepts or incomplete).
     - **`ERROR`**: Network, timeout, or model failure.
4. **Benchmarking & Regression Artifacts**:
   - Exported complete test runs into structured CSV files (`baseline_results.csv`) with release versioning (`v0.1`), enabling repeatable comparison between prompt versions, fine-tuned models, or provider changes.

---

## 📂 Project Structure

```text
Week 6/
├── .env                  # API credentials (ignored by Git)
├── .gitignore            # Excludes secrets and temporary cache
├── baseline_results.csv  # Benchmark output report with individual scores and statuses
├── golden_set.json       # 30-question curated evaluation dataset
├── main.py               # Evaluation runner supporting Gemini API, Ollama, & instant CSV summary
├── README.md             # Documentation, evaluation criteria, and commands
└── requirements.txt      # Dependencies (requests, google-genai, python-dotenv)
```

---

## 🚀 How to Execute

### 1. Run the Evaluation Runner
```powershell
cd "Week 6"
python main.py
```

### 2. Available Execution Modes

#### Option A: Quick View of Baseline Summary (Fastest - instant report)
- When prompted: Type **`3`** and press **`Enter`**.
- Reads existing evaluated benchmark results directly from `baseline_results.csv`:
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

#### Option B: Live Evaluation with Gemini API
- When prompted: Press **`Enter`** (defaults to Gemini `gemini-3.8-flash`).
- When asked how many questions: Press **`Enter`** (runs 5 questions for quick demonstration) or type `all` to run all 30 questions.
- Generates live AI answers, calculates keyword coverage, and updates `baseline_results.csv`.

*(To return to the root folder after running: `cd ..`)*
