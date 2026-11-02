from src.utils import slugify, reverse_words

def test_slugify():
    assert slugify("Hello World") == "hello-world"

def test_reverse_words():
    assert reverse_words("a b c") == "c b a"
