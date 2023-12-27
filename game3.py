import tkinter as tk
from tkinter import messagebox
import random

class WordGuessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Guessing Game")

        self.in_progress = False  # to track if the game is in progress

        self.word_label = tk.Label(self.master, text="Guess the word letter by letter", font=("Helvetica", 16))
        self.word_label.pack(pady=10)

        self.level_label = tk.Label(self.master, text="Choose your level", font=("Helvetica", 14))
        self.level_label.pack(pady=10)

        self.easy_button = tk.Button(self.master, text="Easy", command=lambda: self.start_game("easy"))
        self.easy_button.pack()

        self.medium_button = tk.Button(self.master, text="Medium", command=lambda: self.start_game("medium"))
        self.medium_button.pack()

        self.hard_button = tk.Button(self.master, text="Hard", command=lambda: self.start_game("hard"))
        self.hard_button.pack()

    def start_game(self, difficulty):
        if self.in_progress:
            messagebox.showwarning("Game in Progress", "Finish or quit the current game before starting a new one.")
        else:
            self.in_progress = True
            self.difficulty = difficulty
            self.word_to_guess = random.choice(self.get_word_list(difficulty))
            self.placeholder_word = ["_" for _ in self.word_to_guess]
            self.remaining_attempts = self.calculate_remaining_attempts()

            self.word_label.config(text=" ".join(self.placeholder_word))
            self.level_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")

            self.entry_label = tk.Label(self.master, text="Enter a letter:")
            self.entry_label.pack()

            self.entry_var = tk.StringVar()
            self.entry_box = tk.Entry(self.master, textvariable=self.entry_var, width=5)
            self.entry_box.pack()

            self.submit_button = tk.Button(self.master, text="Submit", command=self.check_guess)
            self.submit_button.pack()

            self.hint_button = tk.Button(self.master, text="Give me a hint", command=self.show_hint)
            self.hint_button.pack()

            self.quit_button = tk.Button(self.master, text="Quit", command=self.quit_game)
            self.quit_button.pack()

    def check_guess(self):
        guess = self.entry_var.get().lower()
        self.entry_var.set("")  # Clear the entry box after each submission

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a valid single letter.")
            return

        if guess in self.word_to_guess:
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == guess:
                    self.placeholder_word[i] = guess
            self.word_label.config(text=" ".join(self.placeholder_word))
            if "_" not in self.placeholder_word:
                messagebox.showinfo("Congratulations", "You guessed the word!")
                self.quit_game()
        else:
            self.remaining_attempts -= 1
            self.level_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")
            if self.remaining_attempts == 0:
                messagebox.showinfo("Game Over", f"Out of attempts. The word was: {self.word_to_guess}")
                self.quit_game()

    def show_hint(self):
        hint = self.get_hint(self.word_to_guess)
        messagebox.showinfo("Hint", hint)

    def calculate_remaining_attempts(self):
        if self.difficulty == "easy":
            return len(self.word_to_guess) + 10
        elif self.difficulty == "medium":
            return len(self.word_to_guess) + 7
        elif self.difficulty == "hard":
            return len(self.word_to_guess) + 4

    def get_word_list(self, difficulty):
        
        if difficulty == "easy":
            return ["apple", "banana", "cherry", "orange", "grape", "pear", "melon", "kiwi"]
        elif difficulty == "medium":
            return ["elephant", "giraffe", "kangaroo", "rhinoceros","zeppelin", "perpendicular", "cataclysmic"]
        elif difficulty == "hard":
            return ["programming", "algorithm", "python", "exponential", "polyglot", "mnemonic", "cacophony", "ubiquitous"]

    def get_hint(self, word):
        
        hints = {"apple": "A common fruit", "banana": "Yellow and long", "cherry": "Small and red",
                  "orange": "A citrus fruit", "grape": "Small, juicy, and often used to make wine", 
                  "pear": "Shaped like a teardrop", "melon": "Large, sweet fruit with a hard rind", 
                  "kiwi": "Small, brown, and fuzzy on the outside", "rhinoceros": "Large herbivorous mammal with one or two horns on its snout",
                  "zeppelin": "A type of rigid airship named after its German inventor", "perpendicular": "Forming an angle of 90 degrees",
                  "cataclysmic": "Involving a sudden and violent upheaval or disaster",
                 "elephant": "Large mammal with a trunk", "giraffe": "Tall with a long neck",
                 "kangaroo": "Hops and has a pouch", "programming": "Writing code for computers",
                 "algorithm": "A step-by-step procedure", "python": "A programming language", "exponential": "Growing rapidly, especially in terms of mathematics",
                 "polyglot": "A person who knows and is able to use several languages",
                 "mnemonic": " A memory aid, especially one that involves patterns or associations",
                 "cacophony": "A harsh, discordant mixture of sounds", "ubiquitous": "Present, appearing, or found everywhere" }
        return hints.get(word, "No hint available")

    def quit_game(self):
        self.in_progress = False  # Reset the game in progress flag
        self.word_label.config(text="")
        self.level_label.config(text="")
        self.entry_label.destroy()
        self.entry_box.destroy()
        self.submit_button.destroy()
        self.hint_button.destroy()
        self.quit_button.destroy()
        self.easy_button.config(state=tk.NORMAL)
        self.medium_button.config(state=tk.NORMAL)
        self.hard_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    game = WordGuessGame(root)
    root.mainloop()
