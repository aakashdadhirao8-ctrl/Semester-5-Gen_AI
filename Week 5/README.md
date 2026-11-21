# Week 5: Token Economics & Budget Capacity Planning

## 🎯 Lab Focus
Perform quantitative token economics modeling, API capacity verification, and financial budget planning before deploying an AI feature to production.

---

## 🧠 What We Have Learnt

1. **Token Economics Modeling**:
   - Calculated expected daily and monthly token consumption from user traffic assumptions:
     $$\text{Daily Input} = \text{Requests/Day} \times \text{Avg Input Tokens}$$
     $$\text{Daily Output} = \text{Requests/Day} \times \text{Avg Output Tokens}$$
     $$\text{Daily Cost} = \frac{\text{Daily Input} \times P_{\text{in}} + \text{Daily Output} \times P_{\text{out}}}{1,000,000}$$
2. **Burst & Concurrency Capacity Planning**:
   - Modeled peak traffic load using **Requests Per Minute (RPM)** and **Tokens Per Minute (TPM)**.
   - Evaluated burst limits against provider tier quotas (e.g. 100 RPM, 50,000 TPM).
3. **Safety Margins**:
   - Integrated configurable safety margins (e.g. 20% traffic surge buffer) to ensure the system does not hit 429 rate limit errors or exceed daily budgets during unexpected traffic spikes.
4. **Automated Planning Gates**:
   - Automated Pass/Review checks across four pillars: RPM Capacity, TPM Capacity, Daily Budget, and Monthly Budget.

---

## 📂 Project Structure

```text
Week 5/
├── .env                  # Capacity & budget parameters (ignored by Git)
├── .env.example          # Parameter template with production defaults
├── .gitignore            # Excludes environment variables and Python cache
├── budget.py             # FeatureBudget dataclass & token economics report generator
├── README.md             # Documentation and economic formulas
├── requirements.txt      # Dependencies (python-dotenv, pytest)
└── test_budget.py        # Automated unit tests testing capacity and budget thresholds
```

---

## 🚀 How to Execute

### 1. Run the Token Economics Report (`budget.py`)
```powershell
cd "Week 5"
python budget.py
```

### 2. Expected Output
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

### 3. Run the Automated Unit Tests (`test_budget.py`)
```powershell
python test_budget.py
```
- **Expected Output**:
  ```text
  ....
  ----------------------------------------------------------------------
  Ran 4 tests in 0.000s

  OK
  ```

*(To return to the root folder after running: `cd ..`)*
