from problem1_rag.app.core.config import RAW_DATA_DIR
from problem1_rag.app.ingestion.document_loader import load_document


def show(filename: str):
    document = load_document(RAW_DATA_DIR / filename)

    print("=" * 60)
    print(document.source.name)
    print(document.file_type)
    print(document.metadata)
    print("-" * 60)
    print(document.text[:300])
    print("=" * 60)
    print()


def main():
    show("sample.pdf")
    show("sample.html")
    show("sample.md")


if __name__ == "__main__":
    main()