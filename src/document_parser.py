
from pathlib import Path

from docx import Document
from pypdf import PdfReader


SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx"}


def extract_text(file_path: str | Path) -> str:
    """Extract text from a TXT, PDF, or DOCX document."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {extension}. "
            "Supported types: TXT, PDF, DOCX."
        )

    if extension == ".txt":
        text = path.read_text(encoding="utf-8-sig")

    elif extension == ".pdf":
        reader = PdfReader(str(path))
        text = "\n".join(
            page.extract_text() or "" for page in reader.pages
        )

    else:
        document = Document(str(path))
        paragraphs = [p.text for p in document.paragraphs]
        text = "\n".join(paragraphs)

    return text.strip()
