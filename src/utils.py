def slugify(text: str) -> str:
    """Lowercase and replace spaces with hyphens."""
    return "-".join(text.strip().lower().split())


def reverse_words(text: str) -> str:
    """Reverse the order of words."""
    return " ".join(text.split()[::-1])


def truncate(text: str, limit: int) -> str:
    """Truncate with ellipsis (BROKEN: off-by-one)."""
    return text[:limit] + "..." if len(text) > limit else text
