
from functools import lru_cache

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def _load_model():
    """Load the semantic model once and reuse it."""
    return SentenceTransformer(MODEL_NAME)


def semantic_similarity(text_a: str, text_b: str) -> float:
    """
    Return semantic similarity as a percentage from 0 to 100.

    This measures meaning similarity, not proof of plagiarism.
    """
    if not isinstance(text_a, str) or not isinstance(text_b, str):
        raise TypeError("Both inputs must be strings.")

    if not text_a.strip() or not text_b.strip():
        raise ValueError("Both texts must contain readable text.")

    model = _load_model()
    embeddings = model.encode(
        [text_a.strip(), text_b.strip()],
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    score = float(cosine_similarity(
        embeddings[0].reshape(1, -1),
        embeddings[1].reshape(1, -1),
    )[0, 0])

    # Convert cosine similarity to a percentage for display.
    return round(max(0.0, min(1.0, score)) * 100, 2)
