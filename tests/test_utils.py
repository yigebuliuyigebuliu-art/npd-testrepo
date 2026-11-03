from src.utils import slugify, reverse_words, count_vowels

def test_slugify():
    assert slugify("Hello World") == "hello-world"

def test_reverse_words():
    assert reverse_words("a b c") == "c b a"

def test_count_vowels():
    assert count_vowels("AEIOU") == 5
    assert count_vowels("Hello World") == 3
    assert count_vowels("bcdfg") == 0
