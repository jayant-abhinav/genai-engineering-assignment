from problem1_rag.app.core.config import RAW_DATA_DIR
from problem1_rag.app.ingestion.pdf_loader import load

def test_pdf_loader():
    document = load(RAW_DATA_DIR / "sample.pdf")

    assert document.file_type == ".pdf"
    assert len(document.text) > 0
    assert document.source.name == "sample.pdf"