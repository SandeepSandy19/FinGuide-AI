---
language:
- en

license: cc-by-4.0

task_categories:
- question-answering
- text-generation
- text-retrieval

task_ids:
- extractive-qa
- open-domain-qa

pretty_name: FinQA-30K

size_categories:
- 10K<n<100K

tags:
- finance
- financial-qa
- rag
- llm
- instruction-tuning
- dataset
- question-answering
- benchmark
- synthetic-data
---

# FinQA-30K

## Overview

FinQA-30K is a large-scale multi-domain financial Question-Answer (QA) dataset designed for:

- Financial NLP research
- Large Language Model (LLM) fine-tuning
- Retrieval-Augmented Generation (RAG)
- Financial Question Answering
- Instruction tuning
- Benchmark evaluation

The dataset contains over **30,000 high-quality question-answer pairs** generated from financial documents spanning **10 financial domains**.

---

# Dataset Statistics

| Property | Value |
|----------|-------|
| Dataset Name | FinQA-30K |
| Domains | 10 |
| Total QA Pairs | 30,000+ |
| Language | English |
| Format | JSON & JSONL |
| Question Types | Factual, Reasoning, Scenario-based, Analytical |

---

# Financial Domains

The dataset is divided into the following domains:

1. Banking
2. Corporate Finance
3. Financial Accounting
4. Financial Markets and Institutions
5. FinTech and Digital Payments
6. Insurance and Actuarial Finance
7. Investment Banking
8. Personal Finance and Wealth Management
9. Risk Management
10. Stock Market

---

# Folder Structure

```
FinQA-30K/

├── banking/
│   ├── banking.json
│   └── banking.jsonl
│
├── corporate_finance/
│   ├── corporate_finance.json
│   └── corporate_finance.jsonl
│
├── financial_accounting/
│   ├── financial_accounting.json
│   └── financial_accounting.jsonl
│
├── financial_markets_and_institutions/
│   ├── financial_markets_and_institutions.json
│   └── financial_markets_and_institutions.jsonl
│
├── fintech_and_digital_payments/
│   ├── fintech_and_digital_payments.json
│   └── fintech_and_digital_payments.jsonl
│
├── insurance_and_actuarial_finance/
│   ├── insurance_and_actuarial_finance.json
│   └── insurance_and_actuarial_finance.jsonl
│
├── investment_banking/
│   ├── investment_banking.json
│   └── investment_banking.jsonl
│
├── personal_finance_and_wealth_management/
│   ├── personal_finance_and_wealth_management.json
│   └── personal_finance_and_wealth_management.jsonl
│
├── risk_management/
│   ├── risk_management.json
│   └── risk_management.jsonl
│
├── stock_market/
│   ├── stock_market.json
│   └── stock_market.jsonl
│
└── README.md
```

---

# File Formats

Each domain contains two versions of the dataset.

### JSON

The `.json` files store the complete dataset as a JSON array.

Example

```json
[
  {
    "source_pdf": "banking_book.pdf",
    "chunk_id": 12,
    "question": "What is CRR?",
    "answer": "Cash Reserve Ratio is...",
    "type": "Factual"
  }
]
```

---

### JSONL

The `.jsonl` files contain one JSON object per line, making them suitable for streaming and large-scale machine learning pipelines.

Example

```json
{"source_pdf":"banking_book.pdf","chunk_id":12,"question":"What is CRR?","answer":"Cash Reserve Ratio...","type":"Factual"}
{"source_pdf":"banking_book.pdf","chunk_id":13,"question":"Why do banks maintain CRR?","answer":"...","type":"Reasoning"}
```

---

# Dataset Schema

Each record contains the following fields.

| Field | Description |
|--------|-------------|
| source_pdf | Original source document |
| chunk_id | Unique chunk identifier |
| question | Generated question |
| answer | Corresponding answer |
| type | Question category |

---

# Question Categories

The dataset includes four different question types.

- Factual
- Reasoning
- Scenario-based
- Analytical

These question types provide balanced coverage of financial reasoning tasks.

---

# Applications

This dataset can be used for

- Financial Question Answering
- Retrieval-Augmented Generation (RAG)
- LLM Fine-tuning
- Instruction Tuning
- Benchmark Evaluation
- Financial Chatbots
- Educational Applications
- Domain-specific NLP Research

---

# Citation

If you use this dataset, please cite:

```bibtex
@article{finqa30k2026,
  title={FinQA-30K: A Multi-Domain Question-Answer Dataset for Financial Knowledge Covering Ten Domains Generated via Large Language Model-Assisted Pipeline},
  year={2026}
}
```

---

# License

This dataset is released under the **CC BY 4.0 License**.

---

# Acknowledgements

This dataset was developed using a modular pipeline consisting of:

- PDF Processing
- Text Cleaning
- Intelligent Chunking
- Metadata Generation
- Gemini Flash Lite-based QA Generation
- Automated Validation
- JSON/JSONL Dataset Construction

The dataset is intended to support research in Financial NLP, Retrieval-Augmented Generation (RAG), and Large Language Models.