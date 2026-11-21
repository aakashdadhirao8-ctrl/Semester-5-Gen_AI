# Week 4: Tokenizer Architectures & Multilingual Analysis

## 🎯 Lab Focus
Compare and analyze the behavior of three primary tokenization algorithms across different language families (English, Telugu, and Hindi) to evaluate token fertility rates, vocabulary efficiency, and multilingual bias.

---

## 🧠 What We Have Learnt

1. **Three Core Subword Tokenization Algorithms**:
   - **Byte Pair Encoding (BPE) (e.g. GPT-2)**: Greedily merges the most frequent pairs of bytes/characters. Highly optimized for English and code, but splits non-Latin scripts into raw UTF-8 byte sequences.
   - **WordPiece (e.g. Multilingual BERT)**: Selects subwords that maximize language model likelihood. Uses `##` prefixes to indicate continuation subword pieces.
   - **SentencePiece (Unigram / BPE) (e.g. XLM-RoBERTa)**: Language-independent tokenization treating whitespace as a regular character (`_` or ` `). Handles non-segmented scripts cleanly.
2. **The "Tokenization Tax" on Indic & Non-Latin Languages**:
   - English sentences require few tokens (typically 8–9 tokens).
   - The exact same sentence in **Telugu** or **Hindi** generates **35 to 76 tokens** in GPT-2's BPE because non-Latin characters are fractured into multiple byte tokens!
   - Shows why multilingual models like **XLM-RoBERTa** are dramatically faster and cheaper for Indic languages (8–10 tokens vs 76 tokens).
3. **Special Tokens & Token IDs**:
   - Analyzed framework-specific delimiters:
     - BERT: `[CLS]` (start of sequence) and `[SEP]` (separator).
     - XLM-RoBERTa: `<s>` (start) and `</s>` (end).

---

## 📂 Project Structure

```text
Week 4/
├── README.md                 # Lab documentation and findings
├── requirements.txt          # Dependencies (transformers, sentencepiece)
└── tokenizer_comparison.py   # Multi-language tokenizer benchmark script with offline fallback
```

---

## 🚀 How to Execute

### 1. Run the Tokenizer Comparison
```powershell
cd "Week 4"
python tokenizer_comparison.py
```

### 2. Expected Output Summary
```text
===========================================================================
WEEK 4: TOKENIZER COMPARISON (BPE vs WordPiece vs SentencePiece)
===========================================================================

LANGUAGE: English
Input: "Artificial intelligence is changing the world."
- BPE - GPT-2                  : 8 tokens
- WordPiece - Multilingual BERT: 9 tokens
- SentencePiece - XLM-R        : 9 tokens

LANGUAGE: Telugu
Input: "కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది."
- BPE - GPT-2                  : 76 tokens  (Severe byte fragmentation!)
- WordPiece - Multilingual BERT: 38 tokens
- SentencePiece - XLM-R        : 8 tokens   (Efficient subword units)

LANGUAGE: Hindi
Input: "कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।"
- BPE - GPT-2                  : 76 tokens  (High token bloat)
- WordPiece - Multilingual BERT: 37 tokens
- SentencePiece - XLM-R        : 10 tokens  (Optimal representation)
```

*(To return to the root folder after running: `cd ..`)*
