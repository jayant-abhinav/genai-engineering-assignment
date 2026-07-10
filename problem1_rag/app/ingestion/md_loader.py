from pathlib import Path
import markdown
from bs4 import BeautifulSoup
from problem1_rag.app.models.document import Document
from problem1_rag.app.ingestion.utils import validate_file

def load(path: Path) -> Document:

    # Extract plain text from a Markdown document.
    validate_file(path, {".md"})

    try:
        md_text = path.read_text(encoding="utf-8")

        html = markdown.markdown(md_text)

        soup = BeautifulSoup(html, "html.parser")

        text = soup.get_text(separator="\n", strip=True)

        return Document(
            source=path,
            file_type=path.suffix.lower(),
            text=text,
            metadata={}
        )

    except Exception as exc:
        raise RuntimeError(f"Failed to read Markdown: {path}") from exc