
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "plagiarism_model.joblib"


def predict_pair(text_a: str, text_b: str, model_path=MODEL_PATH) -> dict:
    """Predict whether a text pair resembles the positive training examples."""
    if not isinstance(text_a, str) or not isinstance(text_b, str):
        raise TypeError("Both inputs must be strings.")

    if not text_a.strip() or not text_b.strip():
        raise ValueError("Both texts must contain non-empty text.")

    model_path = Path(model_path)
    if not model_path.exists():
        raise FileNotFoundError(f"Trained model not found: {model_path}")

    saved = joblib.load(model_path)
    vectorizer = saved["vectorizer"]
    classifier = saved["classifier"]

    vec_a = vectorizer.transform([text_a])
    vec_b = vectorizer.transform([text_b])
    similarity = float(cosine_similarity(vec_a, vec_b)[0, 0])

    features = pd.DataFrame(
        {"cosine_similarity": [similarity]},
        columns=saved["feature_columns"],
    )

    prediction = int(classifier.predict(features)[0])
    probabilities = classifier.predict_proba(features)[0]
    positive_index = list(classifier.classes_).index(1)
    positive_probability = float(probabilities[positive_index])

    return {
        "prediction": prediction,
        "label": (
            "positive-pattern match"
            if prediction == 1
            else "negative-pattern match"
        ),
        "cosine_similarity": similarity,
        "model_positive_probability": positive_probability,
        "warning": (
            "Prototype result only. This model was trained on 10 synthetic "
            "examples and is not reliable evidence of plagiarism."
        ),
    }
