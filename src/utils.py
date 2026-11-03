def slugify(text: str) -> str:
    """Lowercase and replace spaces with hyphens."""
    return "-".join(text.strip().lower().split())


def reverse_words(text: str) -> str:
    """Reverse the order of words."""
    return " ".join(text.split()[::-1])


def truncate(text: str, limit: int) -> str:
    """Truncate with ellipsis (BROKEN: off-by-one)."""
    return text[:limit] + "..." if len(text) > limit else text


def count_vowels(text: str) -> int:
    """Count the vowels in the text.

    BUG: only lowercase vowels are counted, so 'AEIOU' returns 0.
    Expected: both upper- and lower-case vowels are counted (e.g. 'AEIOU' -> 5).
    """
    return sum(1 for ch in text if ch in "aeiou")


def sum_even_numbers(nums):
    """Return the sum of the even numbers in the list.

    BUG: sums all numbers instead of only the even ones.
    Expected: sum_even_numbers([1, 2, 3, 4]) -> 6
    """
    return sum(nums)
