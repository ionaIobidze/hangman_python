import tkinter as tk
from tkinter import messagebox
from helpers import get_word, is_valid_input
from constants import HANGMAN_PICS, INTRO_STR, WIN_MSG, LOSE_MSG


class HangmanGame:
    def __init__(self, master):
        self.master = master
        master.title("Hangman")
        master.configure(bg='black')
        self.canvas = tk.Canvas(master, width=400, height=400, bg='black')
        self.canvas.pack()
        self.display_intro()

        self.secret_word = []
        self.guessed_word = []
        self.lives = 0

        self.label = tk.Label(master, text="Guess the word:", font=("Helvetica", 14), bg='black', fg='white')
        self.label.pack()

        self.word_display = tk.Label(master, text="", font=("Helvetica", 18), bg='black', fg='white')
        self.word_display.pack()

        self.entry = tk.Entry(master, font=("Helvetica", 14))
        self.entry.pack()
        self.entry.bind("<Return>", self.process_input)

        self.restart_button = tk.Button(master, text="Restart", command=self.start_game, font=("Helvetica", 14), bg='grey', fg='black')
        self.restart_button.pack()

        self.start_game()

    def display_intro(self):
        messagebox.showinfo("Hangman", INTRO_STR)

    def start_game(self):
        self.secret_word = list(get_word())
        self.guessed_word = ["_" for _ in self.secret_word]
        self.lives = 5
        self.update_display()
        self.display_hangman()

    def display_hangman(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 200, text=HANGMAN_PICS[5 - self.lives], font=("Courier", 20), fill="white")

    def process_input(self, event):
        input_char = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not is_valid_input(input_char):
            messagebox.showwarning("Invalid Input", "Please provide a valid input (letters from a to z).")
            return

        if input_char in self.secret_word:
            for i, char in enumerate(self.secret_word):
                if input_char == char:
                    self.guessed_word[i] = input_char
            if "_" not in self.guessed_word:
                self.end_game(True)
        else:
            self.lives -= 1
            if self.lives == 0:
                self.end_game(False)

        self.update_display()
        self.display_hangman()

    def update_display(self):
        self.word_display.config(text=" ".join(self.guessed_word))

    def end_game(self, won):
        message = WIN_MSG if won else LOSE_MSG + "\nThe word was: " + "".join(self.secret_word)
        messagebox.showinfo("Game Over", message)
        self.start_game()

