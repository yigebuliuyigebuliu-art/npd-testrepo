from src.utils import slugify, reverse_words, count_vowels, sum_even_numbers, count_consonants

def test_slugify():
    assert slugify("Hello World") == "hello-world"

def test_reverse_words():
    assert reverse_words("a b c") == "c b a"

def test_count_vowels():
    assert count_vowels("AEIOU") == 5
    assert count_vowels("Hello World") == 3
    assert count_vowels("bcdfg") == 0

def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4]) == 6
    assert sum_even_numbers([2, 4, 6]) == 12
    assert sum_even_numbers([1, 3, 5]) == 0
    assert sum_even_numbers([]) == 0

def test_count_consonants():
    assert count_consonants("hello world") == 7
    assert count_consonants("bcdfg") == 5
    assert count_consonants("AEIOU") == 0
    assert count_consonants("") == 0
