# Week 5: Token Economics and Budget Planning

## Objective
Calculate projected token consumption, estimate daily and monthly API costs, and evaluate rate limit capacity (RPM and TPM) with safety margins before deploying an LLM feature.

---

## What I Learnt
- How to estimate daily token load from requests per day and average token lengths:
  Daily Input Tokens = Requests per Day * Average Input Tokens
  Daily Output Tokens = Requests per Day * Average Output Tokens
- How to calculate daily and monthly costs using per-million-token pricing.
- How to check peak concurrency limits against provider quotas (Requests Per Minute and Tokens Per Minute).
- Why adding a safety margin (such as 20%) is necessary to protect against sudden traffic spikes and rate limits.
- How to build dataclasses in Python to validate and report budget checks.

---

## Files
- budget.py: FeatureBudget dataclass that reads parameters from .env and generates the Token Economics Report.
- test_budget.py: Unit tests verifying that cost calculations and capacity checks pass or fail as expected.
- .env: Stores traffic assumptions, pricing, and budget limits.
- .env.example: Template for budget configuration.
- requirements.txt: Package dependencies.

---

## How to Run

### 1. Budget Report
cd "Week 5"
python budget.py

### 2. Unit Tests
python test_budget.py
