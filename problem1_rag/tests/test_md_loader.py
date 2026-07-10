from problem1_rag.app.core.config import RAW_DATA_DIR
from problem1_rag.app.ingestion.md_loader import load

def test_md_loader():
    document = load(RAW_DATA_DIR / "sample.md")

    assert document.file_type == ".md"
    assert len(document.text) > 0
    assert document.source.name == "sample.md"