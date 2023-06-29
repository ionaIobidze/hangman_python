from helpers import (
    display_intro,
    display_end,
    display_hangman,
    get_word,
    is_valid_input,
)


def play():
    secret_word = list(get_word())
    guessed_word = ["_" for _ in secret_word]
    lives = 5
    display_hangman(lives)

    while True:
        print("Guess the word: " + "".join(guessed_word))
        input_char = input("Enter the letter:\n").lower()

        if not is_valid_input(input_char):
            print("Please provide a valid input. (letters from a to z)")
            continue

        if input_char in secret_word:
            for i, char in enumerate(secret_word):
                if input_char == char:
                    guessed_word[i] = input_char
            display_hangman(lives)

            if "_" not in guessed_word:
                print("Hidden word was: " + "".join(secret_word))
                return True
        else:
            lives -= 1
            display_hangman(lives)
            if lives == 0:
                print("Hidden word was: " + "".join(secret_word))
                return False


def hangman():
    while True:
        display_intro()
        result = play()
        display_end(result)

        while True:
            replay = input("Do you want to play again? (yes/no)\n").lower()
            if replay in {"yes", "no"}:
                break
            print("Please provide a valid input.")

        if replay == "no":
            return
