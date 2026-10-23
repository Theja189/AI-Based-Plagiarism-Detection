# AI-Based Plagiarism Detection System

## Project Overview
This project detects potential plagiarism in academic documents using text preprocessing, TF-IDF vectorization, cosine similarity, semantic similarity, and an experimental machine learning classifier.

The application is built with Python and Streamlit. It supports TXT, PDF, and DOCX documents, as well as manually pasted text.

## Features
- Upload TXT, PDF, and DOCX documents.
- Paste text directly for comparison.
- Calculate TF-IDF cosine similarity.
- Analyze semantic similarity.
- Display potentially matching sentences.
- Show experimental machine learning predictions.
- Download plagiarism analysis reports as TXT files.

## Technologies Used
- Python 3.12
- Streamlit
- scikit-learn
- pandas
- Sentence Transformers
- PyPDF
- python-docx
- pytest

## Installation

1. Clone or extract the project.
2. Open the project folder in the terminal.
3. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

From the project root directory, execute:

```bash
streamlit run app/app.py
```

Open the local URL displayed in the terminal.

## Run Tests

```bash
PYTHONPATH=. pytest
```

## Important Limitations
The machine learning classifier was trained on a small synthetic dataset and is experimental. Its predictions must not be treated as proof of plagiarism. Similarity scores indicate textual or semantic overlap, not necessarily academic misconduct.

## Project Structure

- `app/` — Streamlit interface and detection page
- `src/` — Document processing, preprocessing, similarity, prediction, and evaluation
- `data/` — Sample documents and training pairs
- `models/` — Trained experimental classifier
- `tests/` — Automated tests
- `requirements.txt` — Python dependencies
