import pytest

from src.code import up_first, reverse_string

def test_up_first():
    assert up_first('skypro') == 'Skypro'

def test_up_first_for_empty():
    assert up_first('') == ''

# def test_reverse_string_num(numbers):
#     assert reverse_string("123") == numbers
#
#
# def test_reverse_string_let(letters):
#     assert reverse_string("hello") == letters

@pytest.mark.parametrize(
    "val, expected",
    [("hello", "olleh"),
    ("world", "dlrow"),
    ("12345", "54321"),
    ("", ""),
     ])
def test_reverse_string(val, expected):
    assert reverse_string(val) == expected
