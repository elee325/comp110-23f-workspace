"""Game that only completes when you guess the right number"""

#random is package and you are importing random integer with randint
from random import randint

#secret number that is being guessed, random integer btwn 1 and 10
secret: int = randint(1,10)

#asking for guessed number, make sure input for str is converted to int
guess: int = int(input("Guess a number between 1 and 10: "))

number_of_tries: int = 3
tries_count: int = 0

#looping until right number is guessed
while guess != secret and (tries_count < number_of_tries - 1):
    print("Wrong!")
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10!")
    #hinting if number is too high or too low
    if guess > secret: 
        print("Your guess was too high!")
    #even if guess equals secret in the "else" condition, it wouldn't print wrong because if its equal, it wouldn't enter while loop at all
    else:
        print("Your guess was too low!")

    #asking for another answer
    guess = int(input("Guess again: "))
    tries_count += 1
#prints once right number is guessed
if guess == secret:
    print("You got it!")

