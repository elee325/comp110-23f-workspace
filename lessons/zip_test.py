"""Test my zip function."""

__author__: str = "730468571"

from lessons.zip import zip


def test_empty_list():
    """Zip of 1 or more empty lists should return empty list."""
    assert zip([], []) == {}


def test_list_length_1():
    """Testing zip on two lists with one element to make a dictionary."""
    test_keys_list: list[str] = ["bunnies"]
    test_values_list: list[int] = [5]
    assert dict(zip(test_keys_list, test_values_list)) == {'bunnies': 5} 


def test_list_length_greater_than_1():
    """Testing zip on two lists with more than one element."""
    test_keys_list: list[str] = ["bunnies", "rabbits", "bunny", "rabbit"]
    test_values_list: list[int] = [5, 10, 15, 20]
    assert dict(zip(test_keys_list, test_values_list)) == {'bunnies': 5, 'rabbits': 10, 'bunny': 15, 'rabbit': 20}