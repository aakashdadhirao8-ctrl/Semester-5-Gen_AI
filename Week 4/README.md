# Week 4: Tokenizer Comparison

## Objective
Compare how three different tokenizers (BPE from GPT-2, WordPiece from Multilingual BERT, and SentencePiece from XLM-RoBERTa) split the same sentence across English, Telugu, and Hindi.

## What I Learnt
- The differences between Byte Pair Encoding (BPE), WordPiece, and SentencePiece tokenization algorithms.
- How subword tokenization allows models to handle unknown and rare words without expanding vocabulary size infinitely.
- Why non-Latin scripts (like Telugu and Hindi) suffer from a "tokenization tax" in models trained mostly on English, resulting in 4 to 8 times more tokens for the same meaning.
- How multilingual tokenizers like XLM-R handle Indic scripts much more efficiently than GPT-2 (8 tokens vs 76 tokens for Telugu).
- How special tokens like `[CLS]`, `[SEP]`, `<s>`, and `</s>` are used to mark sequence boundaries.

## Files
- `tokenizer_comparison.py`: Python script that tokenizes English, Telugu, and Hindi sentences across all 3 tokenizers and prints token counts and tokens.
- `requirements.txt`: Package dependencies (`transformers`, `sentencepiece`).

## How to Run

```powershell
cd "Week 4"
python tokenizer_comparison.py
```

## Key Findings

- **English** ("Artificial intelligence is changing the world."):
  - GPT-2 (BPE): 8 tokens
  - BERT (WordPiece): 9 tokens
  - XLM-R (SentencePiece): 9 tokens

- **Telugu** ("కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది."):
  - GPT-2 (BPE): 76 tokens (byte fragmentation)
  - BERT (WordPiece): 38 tokens
  - XLM-R (SentencePiece): 8 tokens (best representation)

- **Hindi** ("कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।"):
  - GPT-2 (BPE): 76 tokens
  - BERT (WordPiece): 37 tokens
  - XLM-R (SentencePiece): 10 tokens
