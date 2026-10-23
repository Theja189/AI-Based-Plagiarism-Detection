
from sklearn.feature_extraction.text import TfidfVectorizer


def extract_tfidf_features(
    documents: list[str],
    max_features: int = 5000,
    ngram_range: tuple[int, int] = (1, 2),
):
    """Convert documents into TF-IDF feature vectors."""
    if not documents:
        raise ValueError("At least one document is required.")

    if any(not isinstance(doc, str) for doc in documents):
        raise TypeError("Every document must be a string.")

    if not any(doc.strip() for doc in documents):
        raise ValueError("Documents must contain some text.")

    vectorizer = TfidfVectorizer(
        lowercase=True,
        strip_accents="unicode",
        max_features=max_features,
        ngram_range=ngram_range,
        sublinear_tf=True,
    )

    feature_matrix = vectorizer.fit_transform(documents)

    return vectorizer, feature_matrix


def get_feature_names(vectorizer: TfidfVectorizer) -> list[str]:
    """Return the vocabulary terms learned by a fitted vectorizer."""
    return vectorizer.get_feature_names_out().tolist()
