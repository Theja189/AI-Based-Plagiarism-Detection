
from src.preprocessing import normalize_text, clean_text, split_sentences


def test_normalize_text_removes_extra_whitespace():
    assert normalize_text("  Hello   world  ") == "Hello world"


def test_normalize_text_preserves_punctuation():
    assert normalize_text("Hello! World?") == "Hello! World?"


def test_clean_text_normalizes_unicode_whitespace():
    assert clean_text("Academic\u00a0integrity") == "Academic integrity"


def test_split_sentences():
    result = split_sentences("First sentence. Second sentence! Third sentence?")
    assert result == [
        "First sentence.",
        "Second sentence!",
        "Third sentence?",
    ]


def test_split_sentences_empty_input():
    assert split_sentences("   ") == []


def test_normalize_text_rejects_non_string():
    try:
        normalize_text(None)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError for non-string input")
