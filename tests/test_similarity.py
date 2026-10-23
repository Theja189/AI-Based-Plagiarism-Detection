
import pytest

from src.feature_extraction import extract_tfidf_features
from src.similarity import calculate_similarity, compare_documents


def test_identical_documents_have_similarity_one():
    documents = ["academic integrity protects research"]
    vectorizer, _ = extract_tfidf_features(documents)

    score = compare_documents(
        vectorizer,
        documents[0],
        documents[0],
    )

    assert score == pytest.approx(1.0)


def test_unrelated_documents_have_low_similarity():
    documents = [
        "quantum physics studies particles",
        "gardening requires soil and water",
    ]
    vectorizer, _ = extract_tfidf_features(documents)

    score = compare_documents(vectorizer, documents[0], documents[1])

    assert score == pytest.approx(0.0)


def test_similarity_is_symmetric():
    documents = [
        "machine learning detects patterns",
        "machine learning finds patterns",
    ]
    vectorizer, _ = extract_tfidf_features(documents)

    forward = compare_documents(vectorizer, documents[0], documents[1])
    backward = compare_documents(vectorizer, documents[1], documents[0])

    assert forward == pytest.approx(backward)


def test_different_vector_dimensions_raise_error():
    from scipy.sparse import csr_matrix

    with pytest.raises(ValueError):
        calculate_similarity(csr_matrix([[1, 2]]), csr_matrix([[1, 2, 3]]))
