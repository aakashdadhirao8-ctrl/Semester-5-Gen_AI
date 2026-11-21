import os
import sys
import json
import csv
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# -----------------------------------------
# STEP 1: CONFIGURATION & ENVIRONMENT
# -----------------------------------------
load_dotenv(Path(__file__).parent / ".env")
load_dotenv(Path(__file__).parent.parent / ".env")
load_dotenv()

BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "golden_set.json"
OUTPUT_FILE = BASE_DIR / "baseline_results.csv"

# Load golden questions
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    golden_questions = json.load(file)

print("\n======================================")
print("WEEK 6: BASELINE EVALUATION SYSTEM")
print("======================================")
print(f"Total Golden Questions available: {len(golden_questions)}")
print("\nChoose evaluation mode:")
print("1. Gemini Cloud API (gemini-3.8-flash) [Recommended]")
print("2. Ollama Local Model (qwen2.5-coder:14b)")
print("3. View Pre-computed Baseline Summary Report")

choice = input("\nEnter choice (1/2/3) [Default: 1]: ").strip()

if choice == "3":
    # Display pre-computed results immediately
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, "r", encoding="utf-8-sig") as f:
            reader = list(csv.DictReader(f))
        
        passed = sum(1 for r in reader if r.get("Status") == "PASS")
        review = sum(1 for r in reader if r.get("Status") == "REVIEW")
        errors = sum(1 for r in reader if r.get("Status") == "ERROR")
        scores = [float(r["Score"]) for r in reader if r.get("Score")]
        avg_score = sum(scores) / len(scores) if scores else 0.0

        print("\n======================================")
        print("BASELINE EVALUATION SUMMARY (From CSV)")
        print("======================================")
        print("Release Version: v0.1")
        print(f"Total Questions Evaluated: {len(reader)}")
        print(f"Passed Questions (>=60%): {passed}")
        print(f"Questions for Review (<60%): {review}")
        print(f"Failed / Error Requests: {errors}")
        print(f"Average Keyword Coverage: {avg_score:.2f}%")
        print("CSV Results Path:", OUTPUT_FILE)
        sys.exit(0)
    else:
        print("No previous CSV found. Proceeding with live evaluation.")
        choice = "1"

# Provider selection
if choice in ["2", "ollama"]:
    PROVIDER = "ollama"
    MODEL_NAME = "qwen2.5-coder:14b"
    OLLAMA_URL = "http://localhost:11434/api/generate"
    print(f"\nUsing Local Ollama Model: {MODEL_NAME}")
else:
    PROVIDER = "gemini"
    MODEL_NAME = "gemini-3.5-flash-lite"
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env!")
    from google import genai
    gemini_client = genai.Client(api_key=api_key)
    print(f"\nUsing Google Gemini API Model: {MODEL_NAME}")

# Select number of questions to evaluate
count_input = input("\nHow many questions to run? (e.g. 5, 10, or 'all') [Default: 5]: ").strip().lower()
if count_input in ["all", "30"]:
    selected_questions = golden_questions
elif count_input.isdigit() and int(count_input) > 0:
    selected_questions = golden_questions[:int(count_input)]
else:
    selected_questions = golden_questions[:5]

print(f"Running evaluation on {len(selected_questions)} questions...")

# -----------------------------------------
# STEP 3: FUNCTION TO GET LLM ANSWER
# -----------------------------------------
def get_llm_answer(question):
    if PROVIDER == "gemini":
        response = gemini_client.models.generate_content(
            model=MODEL_NAME,
            contents=question
        )
        return (response.text or "").strip()
    else:
        import requests
        payload = {
            "model": MODEL_NAME,
            "prompt": question,
            "stream": False,
            "options": {"temperature": 0}
        }
        res = requests.post(OLLAMA_URL, json=payload, timeout=120)
        res.raise_for_status()
        return res.json().get("response", "").strip()

# -----------------------------------------
# STEP 4: KEYWORD-BASED SCORING
# -----------------------------------------
def calculate_score(answer, expected_keywords):
    answer_lower = answer.lower()
    matched = [kw for kw in expected_keywords if kw.lower() in answer_lower]
    missing = [kw for kw in expected_keywords if kw.lower() not in answer_lower]

    total_kw = len(expected_keywords)
    score = (len(matched) / total_kw * 100) if total_kw > 0 else 0
    return round(score, 2), matched, missing

# -----------------------------------------
# STEP 5: RUN BASELINE EVALUATION
# -----------------------------------------
results = []
total_score = 0
successful_questions = 0

print("\n======================================")
print("BASELINE EVALUATION RUN STARTED")
print("======================================")

for index, item in enumerate(selected_questions, start=1):
    question_id = item["id"]
    question = item["question"]
    expected_answer = item["expected_answer"]
    keywords = item["keywords"]
    source = item["source"]

    print("\n--------------------------------------")
    print(f"Question {index}/{len(selected_questions)}: [{question_id}]")
    print(f"Question: {question}")

    try:
        answer = get_llm_answer(question)
        score, matched, missing = calculate_score(answer, keywords)
        status = "PASS" if score >= 60 else "REVIEW"

        total_score += score
        successful_questions += 1

        print(f"Matched Keywords : {matched}")
        print(f"Missing Keywords : {missing}")
        print(f"Coverage Score   : {score}% -> [{status}]")

        results.append({
            "Question_ID": question_id,
            "Question": question,
            "Expected_Answer": expected_answer,
            "LLM_Answer": answer,
            "Matched_Keywords": ", ".join(matched),
            "Missing_Keywords": ", ".join(missing),
            "Score": score,
            "Status": status,
            "Source": source,
            "Model": MODEL_NAME,
            "Release": "v0.1"
        })

    except Exception as error:
        print(f"Error fetching answer: {error}")
        results.append({
            "Question_ID": question_id,
            "Question": question,
            "Expected_Answer": expected_answer,
            "LLM_Answer": "",
            "Matched_Keywords": "",
            "Missing_Keywords": ", ".join(keywords),
            "Score": 0,
            "Status": "ERROR",
            "Source": source,
            "Model": MODEL_NAME,
            "Release": "v0.1"
        })

# -----------------------------------------
# STEP 6: SAVE RESULTS TO CSV
# -----------------------------------------
fieldnames = [
    "Question_ID",
    "Question",
    "Expected_Answer",
    "LLM_Answer",
    "Matched_Keywords",
    "Missing_Keywords",
    "Score",
    "Status",
    "Source",
    "Model",
    "Release"
]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# -----------------------------------------
# STEP 7: BASELINE SUMMARY
# -----------------------------------------
average_score = (total_score / successful_questions) if successful_questions > 0 else 0
passed = sum(1 for r in results if r["Status"] == "PASS")
review = sum(1 for r in results if r["Status"] == "REVIEW")
errors = sum(1 for r in results if r["Status"] == "ERROR")

print("\n======================================")
print("BASELINE EVALUATION SUMMARY")
print("======================================")
print("Release Version: v0.1")
print("Model Evaluated:", MODEL_NAME)
print("Questions Tested:", len(selected_questions))
print("Passed Questions (>=60%):", passed)
print("Questions for Review (<60%):", review)
print("Failed Requests:", errors)
print(f"Average Keyword Coverage: {round(average_score, 2)}%")
print(f"Evaluation Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Results saved to: {OUTPUT_FILE}")
print("\nBASELINE RUN COMPLETED SUCCESSFULLY!")
