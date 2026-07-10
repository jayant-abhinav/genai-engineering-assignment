from pathlib import Path
from problem1_rag.app.ingestion.pdf_loader import load
from problem1_rag.app.core.config import RAW_DATA_DIR

def main():
    pdf_path = RAW_DATA_DIR / "sample.pdf"

    document = load(pdf_path)

    print(document.source)
    print(document.file_type)
    print(document.metadata)

    print(document.text[:1000])

    print(len(document.text))

if __name__ == "__main__":
    main()