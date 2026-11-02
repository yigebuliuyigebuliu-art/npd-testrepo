from src.utils import slugify, reverse_words, truncate

def test_slugify():
    assert slugify("Hello World") == "hello-world"

def test_reverse_words():
    assert reverse_words("a b c") == "c b a"

def test_truncate():
    # Issue case: should return exactly limit characters
    assert truncate("abcdef", 3) == "abc"
    # Text shorter than limit should not be changed
    assert truncate("ab", 3) == "ab"
    # Text equal to limit should not be changed
    assert truncate("abc", 3) == "abc"
    # Longer text should be truncated to exactly limit chars
    assert truncate("abcdef", 5) == "abcde"
    # Edge case: limit 0
    assert truncate("abcdef", 0) == ""
