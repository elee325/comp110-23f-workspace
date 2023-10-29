"""EX06 - Practice with Dictionary Functions."""

__author__: str = "730468571"


def invert(dict_to_invert: dict[str, str]) -> dict[str, str]:
    """Function that inverts keys and values of given dictionary."""
    if len(dict_to_invert) == 0:
        return {}
    # inverting dicts
    inverted_dict: dict[str, str] = {}
    for key in dict_to_invert:
        inverted_key = dict_to_invert[key]
        if inverted_key in inverted_dict:
            raise KeyError("Repeated key.")
        inverted_dict[inverted_key] = key
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns most popular color and if tie, returns color that appeared first."""
    color_count: dict[str, str] = {} # Dictionary to keep track of color counts
    most_pop_color = None # Variable to store most popular color
    max_count = 0 # Variable to store max count
    color_order = {} # Keeps track of color order


    for name in input_dict:
        color = input_dict[name]

        if color not in color_order:
            color_order[color] = len(color_order) # Order specific color based on if its already been added
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

        # Check if current color is more pop or equal pop as current most pop
        if color_count[color] > max_count or (color_count[color] == max_count and color_order[color] < color_order[most_pop_color]):
            most_pop_color = color
            max_count = color_count[color]
        
    return most_pop_color


def count(input_list: list[str]) -> dict[str, int]:
    """Gives unique keys from list and counts # of times they appear."""
    count_dict: dict[str, int] = {} # dictionary keeping count of unique values
    for key in input_list:
        if key in count_dict:
            count_dict[key] += 1
        else: 
            count_dict[key] = 1

    return count_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Gives dict where each key is unique letter and each value is list of words that begin with that letter."""
    alphabet_dict: dict[str, list[str]] = {}
    for word in input_list:
        # Storing first letter of word
        first_letter = word[0].lower() # Convert to lowercase

        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(word)
        else:
            alphabet_dict[first_letter] = [word]

    return alphabet_dict


def update_attendance(attendance_log: dict[str, list[str]], weekday: str, student: str) -> dict[str, list[str]]:
    """Updates attendance then returns new attendance log."""
    # seeing if day is in attendance log then add student, if not, add it and students
    if weekday in attendance_log:
        attendance_log[weekday].append(student)
    else:
        attendance_log[weekday] = [student]

    return attendance_log
