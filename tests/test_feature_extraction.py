
import pytest

from src.feature_extraction import (
    extract_tfidf_features,
    get_feature_names,
)


def test_tfidf_creates_one_row_per_document():
    documents = [
        "artificial intelligence",
        "academic plagiarism detection",
    ]

    vectorizer, matrix = extract_tfidf_features(documents)

    assert matrix.shape[0] == 2
    assert matrix.shape[1] > 0
    assert len(get_feature_names(vectorizer)) == matrix.shape[1]


def test_tfidf_supports_bigrams():
    documents = [
        "academic plagiarism detection",
        "academic writing research",
    ]

    vectorizer, _ = extract_tfidf_features(documents)
    features = get_feature_names(vectorizer)

    assert "academic plagiarism" in features


def test_empty_document_list_raises_error():
    with pytest.raises(ValueError):
        extract_tfidf_features([])


def test_blank_documents_raise_error():
    with pytest.raises(ValueError):
        extract_tfidf_features(["   ", ""])


def test_non_string_document_raises_error():
    with pytest.raises(TypeError):
        extract_tfidf_features(["valid text", None])
