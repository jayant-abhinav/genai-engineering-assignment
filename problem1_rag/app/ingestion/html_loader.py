from pathlib import Path
from bs4 import BeautifulSoup
from problem1_rag.app.models.document import Document
from problem1_rag.app.ingestion.utils import validate_file

def load(path: Path) -> Document:
    """
    Extract visible text from an HTML document.

    Args:
        path: Path to the HTML file.

    Returns:
        Document object containing extracted text.

    Raises:
        FileNotFoundError:
            If the file does not exist.

        ValueError:
            If the file is not an HTML file.

        RuntimeError:
            If the HTML cannot be processed.
    """

    validate_file(path, {".htm", ".html"})

    try:
        html = path.read_text(encoding="utf-8")

        soup = BeautifulSoup(html, "html.parser")

        # Remove unwanted elements
        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator="\n", strip=True)

        return Document(
            source=path,
            file_type=path.suffix.lower(),
            text=text,
            metadata={}
        )

    except Exception as exc:
        raise RuntimeError(f"Failed to read HTML: {path}") from exc