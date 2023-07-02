import random
import string


def get_word():
    with open("hangman-words.txt") as f:
        words = [line.strip() for line in f]
    return random.choice(words)


def is_valid_input(char):
    return char in string.ascii_lowercase
