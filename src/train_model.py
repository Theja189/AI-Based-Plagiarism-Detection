
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.pipeline import FeatureUnion


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "sample_pairs.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "plagiarism_model.joblib"


def build_pair_features(text_a, text_b, vectorizer):
    """Build TF-IDF vectors and cosine similarity for text pairs."""
    vec_a = vectorizer.transform(text_a)
    vec_b = vectorizer.transform(text_b)

    similarities = []
    for index in range(vec_a.shape[0]):
        score = cosine_similarity(
            vec_a[index], vec_b[index]
        )[0, 0]
        similarities.append(score)

    return pd.DataFrame({"cosine_similarity": similarities})


def train_model(data_path=DATA_PATH, model_path=MODEL_PATH):
    """Train and save a baseline pair-classification model."""
    df = pd.read_csv(data_path)

    required = {"text_a", "text_b", "label"}
    if not required.issubset(df.columns):
        raise ValueError(f"Dataset must contain columns: {sorted(required)}")

    df = df.dropna(subset=["text_a", "text_b", "label"]).copy()
    df["text_a"] = df["text_a"].astype(str)
    df["text_b"] = df["text_b"].astype(str)
    df["label"] = df["label"].astype(int)

    if len(df) < 4 or df["label"].nunique() != 2:
        raise ValueError("Training requires at least 4 labeled pairs from both classes.")

    # Fit vocabulary on both texts from the training examples.
    all_texts = pd.concat([df["text_a"], df["text_b"]], ignore_index=True)
    vectorizer = TfidfVectorizer(
        lowercase=True,
        strip_accents="unicode",
        ngram_range=(1, 2),
        max_features=5000,
        sublinear_tf=True,
    )
    vectorizer.fit(all_texts)

    features = build_pair_features(df["text_a"], df["text_b"], vectorizer)
    model = LogisticRegression(class_weight="balanced", random_state=42)
    model.fit(features, df["label"])

    model_path = Path(model_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        {
            "vectorizer": vectorizer,
            "classifier": model,
            "feature_columns": ["cosine_similarity"],
        },
        model_path,
    )

    return model, features, df["label"]


if __name__ == "__main__":
    model, features, labels = train_model()
    print(f"Training examples: {len(labels)}")
    print(f"Feature shape: {features.shape}")
    print(f"Classes learned: {sorted(model.classes_.tolist())}")
    print(f"Model saved to: {MODEL_PATH}")
    print("Note: this tiny synthetic dataset is only for pipeline testing.")
