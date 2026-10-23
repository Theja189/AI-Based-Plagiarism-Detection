
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import issparse


def calculate_similarity(vector_a, vector_b) -> float:
    """Calculate cosine similarity between two feature vectors."""
    if vector_a.shape[0] != 1 or vector_b.shape[0] != 1:
        raise ValueError("Each input must contain exactly one vector.")

    if vector_a.shape[1] != vector_b.shape[1]:
        raise ValueError("Feature vectors must have the same dimensions.")

    if issparse(vector_a) or issparse(vector_b):
        if vector_a.nnz == 0 or vector_b.nnz == 0:
            return 0.0
    else:
        if not vector_a.any() or not vector_b.any():
            return 0.0

    score = cosine_similarity(vector_a, vector_b)[0, 0]
    return float(max(0.0, min(1.0, score)))


def compare_documents(vectorizer, document_a: str, document_b: str) -> float:
    """Compare two documents using an already-fitted TF-IDF vectorizer."""
    vectors = vectorizer.transform([document_a, document_b])
    return calculate_similarity(vectors[0], vectors[1])
