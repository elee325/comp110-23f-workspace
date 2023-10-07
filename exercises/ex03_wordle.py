"""Structured Wordle with Function Loops and Guesses."""

__author__: str = "730468571"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"   


# fn for if character is found in a word
def contains_char(searched_word: str, searched_char: str) -> bool:
    """Returns True if chr is found in word."""
    assert len(searched_char) == 1
    searched_word_idx: int = 0
    # loop for checking each index with chr to return bool
    while searched_word_idx < len(searched_word):
        if searched_word[searched_word_idx] == searched_char:
            return True
        searched_word_idx += 1
    return False


# fn for coding emojis to indicate correct letters
def emojified(guessed_word: str, secret_word: str) -> str:
    """Reveals emojis to indicate how chrs match up in two strs."""
    assert len(guessed_word) == len(secret_word)
    emoji_line: str = ""
    idx: int = 0
    # similar to one shot wordle
    while idx < len(secret_word):
        if guessed_word[idx] == secret_word[idx]:
            emoji_line += GREEN_BOX
        else:
            if contains_char(secret_word, guessed_word[idx]):
                emoji_line += YELLOW_BOX
            else:
                emoji_line += WHITE_BOX
        idx += 1
    return emoji_line


# fn for providing guess of right length
def input_guess(expected_length: int) -> str:
    """Makes sure guess matches length of secret word."""
    guess: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(guess) != expected_length:
        guess = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    else:
        return guess


# main function is to have secret word as variable, keep track of turns, and whether player has won
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # start at zero technically but 1 for Turn 1/6
    current_turn: int = 1
    secret_word: str = "codes"

# showing turns and asking for guess
    while current_turn <= 6:
        print("=== Turn " + str(current_turn) + "/6 ===")
        guess: str = input_guess(len(secret_word))
    
    # if guess matches secret word
        if guess == secret_word:
            print(emojified(guess, secret_word))
            print("You won in " + str(current_turn) + "/6 turns!")
            return

        # asking for another turn
        if guess != secret_word:
            print(emojified(guess, secret_word))
            current_turn += 1


# run out of turns
        if guess != secret_word and current_turn > 6:
            print("X/6 - Sorry, try again tomorrow!")
            return


# allows to run file as module
if __name__ == "__main__":
    main()