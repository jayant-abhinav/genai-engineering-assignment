from problem1_rag.app.core.config import RAW_DATA_DIR
from problem1_rag.app.ingestion.html_loader import load

def test_html_loader():
    document = load(RAW_DATA_DIR / "sample.html")

    assert document.file_type == ".html"
    assert len(document.text) > 0
    assert document.source.name == "sample.html"