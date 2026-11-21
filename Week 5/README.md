# Week 5: Token Economics and Budget Planning

## Objective
Calculate projected token consumption, estimate daily and monthly API costs, and evaluate rate limit capacity (RPM and TPM) with safety margins before deploying an LLM feature.

## What I Learnt
- How to estimate daily token load from requests per day and average token lengths:
  - Daily Input Tokens = Requests/Day * Avg Input Tokens
  - Daily Output Tokens = Requests/Day * Avg Output Tokens
- How to calculate daily and monthly costs using per-million-token pricing.
- How to check peak concurrency limits against provider quotas (Requests Per Minute and Tokens Per Minute).
- Why adding a safety margin (e.g., 20%) is necessary to protect against sudden traffic spikes and rate limits.
- How to build dataclasses in Python to validate and report budget checks.

## Files
- `budget.py`: `FeatureBudget` dataclass that reads parameters from `.env` and generates the Token Economics Report.
- `test_budget.py`: Unit tests verifying that cost calculations and capacity checks pass or fail as expected.
- `.env`: Holds traffic assumptions, pricing, and budget limits.
- `.env.example`: Template for budget configuration.
- `requirements.txt`: Package dependencies (`python-dotenv`, `pytest`).

## How to Run

### 1. Run the Budget Report
```powershell
cd "Week 5"
python budget.py
```

Expected output:
```text
TOKEN ECONOMICS REPORT
-----------------------------------
Input tokens/day:  1,000,000
Output tokens/day: 500,000
Total tokens/day:  1,500,000
Estimated daily cost:   $1.5500
Estimated monthly cost: $46.50
Peak RPM with margin: 12.0
Peak TPM with margin: 18000

CHECKS
RPM capacity: PASS
TPM capacity: PASS
Daily budget: PASS
Monthly budget: PASS

Recommendation: WITHIN configured planning limits.
```

### 2. Run the Unit Tests
```powershell
python test_budget.py
```
Expected output:
```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
