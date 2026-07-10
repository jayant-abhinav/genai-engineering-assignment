from problem1_rag.app.core.config import RAW_DATA_DIR
from problem1_rag.app.ingestion.document_loader import load_document


def test_document_loader():
    document = load_document(RAW_DATA_DIR / "sample.md")

    assert document.file_type == ".md"
    assert len(document.text) > 0