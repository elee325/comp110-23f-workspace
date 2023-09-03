"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730468571"

# initialize asking for word input
guessed_word: str = input("Enter a 5-character word: ")

# exiting when less than 5-char
if len(guessed_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

# initialize asking for single character
guessed_char: str = input("Enter a single character: ")

# exiting when not single character
if len(guessed_char) != 1:
    print("Error: Character must be a single character.")
    exit()

# initialize counting number of matching characters
num_of_matches: int = 0

# searching for single chr in word
print("Searching for " + guessed_char + " in " + guessed_word)

# checking index for matches
if guessed_char == guessed_word[0]:
    print(guessed_char + " found at index 0")
# increasing number of matches if letter found
    num_of_matches += 1
  

if guessed_char == guessed_word[1]:
    print(guessed_char + " found at index 1")
    num_of_matches += 1


if guessed_char == guessed_word[2]:
    print(guessed_char + " found at index 2")
    num_of_matches += 1

if guessed_char == guessed_word[3]:
    print(guessed_char + " found at index 3")
    num_of_matches += 1

if guessed_char == guessed_word[4]:
    print(guessed_char + " found at index 4")
    num_of_matches += 1

# presenting number of matched letters when 1
if num_of_matches == 1:
    print(str(num_of_matches) + " instance of " + guessed_char + " found in " + guessed_word)

# presenting number of matched letters when 2
if num_of_matches > 1:
    print(str(num_of_matches) + " instances of " + guessed_char + " found in " + guessed_word)

# presenting number of matched letters when none found
if num_of_matches == 0:
    print("No instances of " + guessed_char + " found in " + guessed_word)

