import re


def sanitize(text: str) -> str:
    """
    Sanitize a string to be safe for filesystem usage.

    Removes or replaces characters that are invalid in file names
    across different operating systems.

    Args:
        text: Raw string (e.g., track title or artist name)

    Returns:
        Sanitized string safe for file paths
    """
    return re.sub(r'[<>:"/\\|?*]', "_", text)
