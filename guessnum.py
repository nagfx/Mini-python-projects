# guess the random number game using random library
import random

# making a random function


def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("Sorry, guess again it is too low.")
        elif guess > random_num:
            print("Sorry, guess again it is too high")
    print(f"Hurray! You have guessed the number {random_num} correctly!!")


def computer_guess(x):
    lower = 1
    higher = x
    feedback = ""
    while feedback != "c":
        if lower != higher:
            guess = random.randint(lower, higher)
        else:
            guess = lower
        feedback = input(
            f"Is {guess} too high (H), too low (L) or correct (C)?? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print("The AI has guessed your number {guess} rightly!")


computer_guess(10)
