
title: Financial Document QA Dataset
tags:
  - financial-documents
  - question-answering
  - tabular-data
  - machine-learning
license: apache-2.0
datasets:
  - financial-document-qa
language: en
---

# **ConvFinQA: Financial Document QA Dataset**

### **Dataset Summary**

The ConvFinQA dataset and code from EMNLP 2022 paper(https://arxiv.org/abs/2210.03849)

### **Dataset Features**

- **Pre-text**: Contextual paragraphs that precede a table, giving information relevant to the financial table.
- **Post-text**: Context that follows the table, providing additional explanation or details.
- **Filename**: The source PDF filename from which the data was extracted.
- **Table_ori**: The original table content as it appears in the document.
- **Table**: The cleaned and normalized table format for easier data consumption.
- **QA**: Structured question-answer pairs, including reasoning steps and annotated text from the document.

### **Dataset Structure**

This dataset is provided in a `DatasetDict` with `train` and `test` splits:

- **Train Dataset**: Contains structured data from financial documents, designed for training machine learning models.
- **Test Dataset**: The first 200 elements from the training data are selected for validation purposes.
  
Each split contains the following fields:
- **pre_text**: `List[str]`
- **post_text**: `List[str]`
- **filename**: `str`
- **table_ori**: `List[List[str]]`
- **table**: `List[List[str]]`
- **question**: `str`
- **answer**: `str`
- **steps**: `List[dict]`
- **id**: `str`

### **Example Data**
Here’s a quick look at the data format:

```json
{
  "pre_text": ["value , which may be maturity ..."],
  "post_text": ["."],
  "filename": "VRTX/2005/page_103.pdf",
  "table_ori": [["", "2005", "2004"], ["Furniture and equipment", "$98,387", "$90,893"]],
  "table": [["", "2005", "2004"], ["furniture and equipment", "$ 98387", "$ 90893"]],
  "question": "What is the percent change in net loss on disposal of assets between 2004 and 2005?",
  "answer": "700%",
  "steps": [
    {"op": "minus1-1", "arg1": "344000", "arg2": "43000", "res": "301000"},
    {"op": "divide1-2", "arg1": "#0", "arg2": "43000", "res": "700%"}
  ],
  "id": "Single_VRTX/2005/page_103.pdf-1"
}
```

### **Use Cases**

1. **Question-Answering**: The dataset is ideal for training models that can answer complex questions about financial data and documents.
2. **Table Understanding**: The cleaned tables provide a clear format for understanding structured tabular data.
3. **Financial Document Parsing**: Can be used to develop models that parse financial documents and extract relevant information.

### **Loading the Dataset**

You can load the dataset from the Hugging Face Hub using the following code:

```python
from datasets import load_dataset

dataset = load_dataset("MehdiHosseiniMoghadam/financial-document-qa")
```

ref: https://github.com/czyssrs/ConvFinQA/tree/main?tab=readme-ov-file
```

---

You can adjust the title and citation information as necessary depending on the specific details of your dataset. Once your dataset is uploaded to the Hugging Face Hub, it will also automatically generate some sections like usage, but this card will help structure important information about your dataset!