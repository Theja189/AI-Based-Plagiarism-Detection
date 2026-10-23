
import pytest

from src.semantic_similarity import semantic_similarity


def test_identical_text_has_100_percent_similarity():
    text = "Artificial intelligence helps students learn."
    assert semantic_similarity(text, text) == 100.0


def test_empty_text_raises_error():
    with pytest.raises(ValueError):
        semantic_similarity("", "Some text")


def test_non_string_input_raises_error():
    with pytest.raises(TypeError):
        semantic_similarity(None, "Some text")
