# rock paper scissors game
import random


def game():
    user = input(
        "What is your choice 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

    if is_winning(user, computer):
        return "You won!"

    return "You lost!"


def is_winning(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(game())
