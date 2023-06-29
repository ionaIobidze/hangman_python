import random
import string


def display_intro():
    from constants import INTRO_STR

    print(INTRO_STR)


def display_end(result):
    from constants import WIN_MSG, LOSE_MSG

    if result:
        print(WIN_MSG)
    else:
        print(LOSE_MSG)


def display_hangman(state):
    from constants import HANGMAN_PICS

    print(HANGMAN_PICS[state])


def get_word():
    with open("hangman-words.txt") as f:
        words = [line.strip() for line in f]
    return random.choice(words)


def is_valid_input(char):
    return char in string.ascii_lowercase
