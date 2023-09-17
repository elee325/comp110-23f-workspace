"""EX02 - One Shot Wordle with Emojis."""

__author__: str = "730468571"

secret_word: str = "python"
# assigning length of secret word to variable
secret_length: int = len(secret_word)
# index for secret word
secret_idx: int = 0

# asking for guess
guessed_word: str = input(f"What is your {secret_length}-letter guess? ")

# index for checking guessed word
guessed_idx: int = 0
# emojis for guesses
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

emoji_line: str = ""

# looping until guessed word is right amnt of chrs
while len(guessed_word) != secret_length:
    guessed_word = input(f"That was not {secret_length} letters! Try again: ")

# loop to check matching letters
while guessed_idx < secret_length:
    if guessed_word[guessed_idx] == secret_word[secret_idx]:
        emoji_line += GREEN_BOX
    else:
        # boolean variable for guessed character in word elsewhere
        chr_exists = False
        # keep track of alternate indices of secret
        alt_secret_idx: int = 0
        # loop for checking if letters present elsewhere in word
        while not chr_exists and alt_secret_idx < secret_length:
            if secret_word[alt_secret_idx] == guessed_word[guessed_idx] and alt_secret_idx != secret_idx:
                chr_exists = True
            else: 
                alt_secret_idx += 1
        if chr_exists:
            emoji_line += YELLOW_BOX
        else: 
            emoji_line += WHITE_BOX

    # increase index variable
    guessed_idx += 1
    secret_idx += 1
print(emoji_line)

# after loop when guessed word has right amount of characters    
if guessed_word != secret_word:
    print("Not quite. Play again soon!")
if guessed_word == secret_word:
    print("Woo! You got it! ")

    