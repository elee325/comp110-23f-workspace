"""Practice with functions in class."""


def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx."""
    if letter_idx < len(my_words):
        return my_words[letter_idx]
    else:
        if letter_idx >= len(my_words):
            return ("Too high of an index") 


print(mimic_letter("hi", 3))