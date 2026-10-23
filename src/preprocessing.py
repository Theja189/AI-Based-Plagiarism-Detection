
import re
import unicodedata


def normalize_text(text: str) -> str:
    """Normalize Unicode and whitespace while preserving word content."""
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_text(text: str) -> str:
    """Clean extracted document text without removing meaningful words."""
    text = normalize_text(text)
    text = re.sub(r"[\u200b-\u200f\uFEFF]", "", text)
    return text


def split_sentences(text: str) -> list[str]:
    """Split text into sentences using basic punctuation rules."""
    text = clean_text(text)

    if not text:
        return []

    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]
