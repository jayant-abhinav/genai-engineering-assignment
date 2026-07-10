from pathlib import Path

def validate_file(path: Path, allowed_extensions: set[str]) -> None:
    """
    Validate that a file exists and has an allowed extension.

    Args:
        path: File path.
        allowed_extensions: Allowed file extensions.

    Raises:
        FileNotFoundError:
            If the file does not exist.

        ValueError:
            If the extension is not supported.
    """

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    suffix = path.suffix.lower()

    if suffix not in allowed_extensions:
        raise ValueError(
            f"Expected one of {allowed_extensions}, got '{suffix}'"
        )