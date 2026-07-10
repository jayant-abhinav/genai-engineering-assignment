from pathlib import Path
from pypdf import PdfReader
from problem1_rag.app.models.document import Document
from problem1_rag.app.ingestion.utils import validate_file

def load(path: Path) -> str:
    """
    Extract text from a PDF document.

    Args:
        path: Path to the PDF file.

    Returns:
        Extracted text as a single string.

    Raises:
        FileNotFoundError:
            If the file does not exist.

        ValueError:
            If the file is not a PDF.

        RuntimeError:
            If the PDF cannot be read.
    """

    validate_file(path, {".pdf"})

    try:
        reader = PdfReader(path)

        pages = []

        for page in reader.pages:
            pages.append(page.extract_text() or "")

        return Document(
            source=path,
            file_type=path.suffix.lower(),
            text="\n".join(pages),
            metadata={
                "pages": len(reader.pages)
            }
        )

    except Exception as exc:
        raise RuntimeError(f"Failed to read PDF: {path}") from exc