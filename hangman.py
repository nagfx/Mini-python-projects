# Hangman game uses words.py file
import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 8

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left. You have used the following letters: ",
              "".join(used_letters))

        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", "".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Letter is not in word")

        elif user_letter in used_letters:
            print("You have used already this character please try again")

        else:
            print("Invalid character. Please try again")

    if lives == 0:
        print("OOps you died the word was", word)
    else:
        print("Oh you guessed it right! The word was: ", word, "!!")


user_input = input("Type something here: ")
print(user_input)
hangman()
