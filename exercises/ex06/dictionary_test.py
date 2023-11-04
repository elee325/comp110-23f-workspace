"""EX07 - Testing Dictionaries."""

__author__: str = "730468571"

from exercises.ex06.dictionary import invert

def test_empty_dict():
    """Empty input dict should return empty dict; edge case."""
    assert invert([]) == {}


def test_dict_length_1():
    """Testing invert on dict with one pair."""
    test_input_dict: dict[str, str] = {"World": "Hello"}
    assert invert(test_input_dict) == {"Hello": "World"}


def test_dict_length_2():
    """Testing invert on dict with 2 pairs."""
    test_input_dict: dict[str, str] = {"honey": "bun", "cup": "cake"}
    assert invert(test_input_dict) == {"bun": "honey", "cake": "cup"}


from exercises.ex06.dictionary import favorite_color

def test_dict_len_1():
    """Testing favorite color on dict with one pair; edge case."""
    test_input_dict: dict[str, str] = {"James": "blue"}
    assert favorite_color(test_input_dict) == "blue"


def test_dict_length_3():
    """Testing favorite_color on dict with three pairs."""
    test_input_dict: dict[str, str] = {"James": "blue", "Frank": "pink", "Jess": "pink"}
    assert favorite_color(test_input_dict) == "pink"


def test_dict_tie():
    """Testing favorite_color on dict with tie for favorite color."""
    test_input_dict: dict[str, str] = {"James": "blue", "Frank": "pink", "Jess": "pink", "Bella": "blue"}
    assert favorite_color(test_input_dict) == "blue"


from exercises.ex06.dictionary import count


def test_count_empty():
    """Testing count on list with no entry; edge case."""
    test_input_list: list[str] = []
    assert count(test_input_list) == {}


def test_count_3():
    """Testing count on a list with 3 entries."""
    test_input_list: list[str] = ["goat", "goat", "llama"]
    assert count(test_input_list) == {"goat": 2, "llama": 1}


def test_count_mult():
    """Testing count on a list with multiple entries."""
    test_input_list: list[str] = ["milk", "milk", "juice", "milk", "water", "juice", "soda"]
    assert count(test_input_list) == {"milk": 3, "juice": 2, "water": 1, "soda": 1} 


from exercises.ex06.dictionary import alphabetizer

def test_list_empty():
    """Testing alphabetizer on an empty list; edge case."""
    test_input_list: list[str] = []
    assert alphabetizer(test_input_list) == {}


def test_list_two_letters():
    """Testing alphabetizer on a list with two unique letters."""
    test_input_list: list[str] = ["jokes", "jam", "Mom", "jersey", "milk"]
    assert alphabetizer(test_input_list) == {'j': ['jokes', 'jam', 'jersey'], 'm': ['Mom', 'milk']}


def test_list_mult_letters():
    """Testing alphabetizer on a list with multiple unique letters."""
    test_input_list: list[str] = ["bananas", "apples", "zebra", "juice", "Abraham", "zesty", "candle", "alive"]
    assert alphabetizer(test_input_list) == {'b': ['bananas'], 'a': ['apples', 'Abraham', 'alive'], 'z': ['zebra', 'zesty'], 'j': ['juice'], 'c': ['candle']}


from exercises.ex06.dictionary import update_attendance

def test_empty_log():
    """Testing update_attendance when attendance_log is empty, should return empty dict. Edge case."""
    test_input_dict: dict[str, list[str]] = {}
    weekday: str = "Monday"
    student: str = "Jamie"
    assert update_attendance(test_input_dict, weekday, student) == {}


def test_one_day_and_name():
    """Testing update_attendance on adding/updating one day and one name."""
    test_input_dict: dict[str, list[str]] = {"Monday": ["Lee", "Cam"], "Tuesday": ["Lee", "Cam", "Mark"]}
    weekday: str = "Wednesday"
    student: str = "Katie"
    assert update_attendance(test_input_dict, weekday, student) == {"Monday": ["Lee", "Cam"], "Tuesday": ["Lee", "Cam", "Mark"], "Wednesday": ["Katie"]}


def test_add_name():
    """Testing update_attendance on adding name to existing day."""
    test_input_dict: dict[str, list[str]] = {"Monday": ["Lee", "Cam"], "Tuesday": ["Lee", "Cam", "Mark"]}
    weekday: str = "Monday"
    student: str = "Jerome"
    assert update_attendance(test_input_dict, weekday, student) == {"Monday": ["Lee", "Cam", "Jerome"], "Tuesday": ["Lee", "Cam", "Mark"]}