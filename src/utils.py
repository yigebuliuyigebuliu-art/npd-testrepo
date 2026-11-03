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
    """Count the vowels in the text (case-insensitive).

    Both upper- and lower-case vowels are counted (e.g. 'AEIOU' -> 5).
    """
    return sum(1 for ch in text if ch in "aeiouAEIOU")


def sum_even_numbers(nums):
    """Return the sum of the even numbers in the list.

    Example: sum_even_numbers([1, 2, 3, 4]) -> 6
    """
    return sum(n for n in nums if n % 2 == 0)


def count_consonants(text: str) -> int:
    """Count the consonants in the text (case-insensitive).

    A consonant is a letter that is not a vowel; spaces and punctuation are
    NOT consonants. Example: count_consonants("hello world") -> 7
    """
    return sum(1 for ch in text.lower() if ch not in "aeiou")
