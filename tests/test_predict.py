
import pytest

from src.predict import predict_pair


def test_predict_pair_returns_expected_fields():
    result = predict_pair(
        "Artificial intelligence helps detect plagiarism.",
        "Artificial intelligence helps identify plagiarism.",
    )

    assert result["prediction"] in (0, 1)
    assert 0.0 <= result["cosine_similarity"] <= 1.0
    assert 0.0 <= result["model_positive_probability"] <= 1.0
    assert "prototype" in result["warning"].lower()


def test_predict_pair_rejects_empty_text():
    with pytest.raises(ValueError):
        predict_pair("", "Some academic text")


def test_predict_pair_rejects_non_string():
    with pytest.raises(TypeError):
        predict_pair(None, "Some academic text")
