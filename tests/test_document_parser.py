
from pathlib import Path

from docx import Document
from reportlab.pdfgen import canvas

from src.document_parser import extract_text


def test_extract_text_from_txt(tmp_path: Path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "Artificial intelligence protects academic integrity.",
        encoding="utf-8",
    )

    assert "academic integrity" in extract_text(file_path)


def test_extract_text_from_docx(tmp_path: Path):
    file_path = tmp_path / "sample.docx"

    doc = Document()
    doc.add_paragraph("Artificial intelligence protects academic integrity.")
    doc.save(file_path)

    assert "academic integrity" in extract_text(file_path)


def test_extract_text_from_pdf(tmp_path: Path):
    file_path = tmp_path / "sample.pdf"

    pdf = canvas.Canvas(str(file_path))
    pdf.drawString(72, 750, "Artificial intelligence protects academic integrity.")
    pdf.save()

    assert "academic integrity" in extract_text(file_path)


def test_missing_file_raises_error(tmp_path: Path):
    missing_file = tmp_path / "missing.txt"

    try:
        extract_text(missing_file)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("Expected FileNotFoundError")


def test_unsupported_file_type_raises_error(tmp_path: Path):
    file_path = tmp_path / "sample.csv"
    file_path.write_text("sample data", encoding="utf-8")

    try:
        extract_text(file_path)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
