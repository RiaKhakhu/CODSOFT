import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

"""
GUI-based ROCK-PAPER-SCISSORS game
AUTHOR: Khakhu Ria
VERSION: 28/09/2024

"""


class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("500x500")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.player_score = 0
        self.computer_score = 0
        self.current_round = 0

        self.main_frame = ttk.Frame(self.master, padding="20", width=500, height=500)
        self.main_frame.grid(row=0, column=0)
        self.main_frame.grid_propagate(False)  # Prevent the frame from resizing

        self.result_var = tk.StringVar()
        self.result_var.set("ROCK PAPER SCISSORS! Make your choice to start the game.")

        # Spinbox for user to select number of rounds
        self.rounds_var = tk.IntVar(value=1)
        self.spinbox_label = ttk.Label(self.main_frame, text="Choose number of rounds:")
        self.spinbox_label.grid(row=1, column=0, pady=(10, 0), sticky="e")
        self.spinbox = ttk.Spinbox(self.main_frame, from_=1, to=100, textvariable=self.rounds_var, width=5)
        self.spinbox.grid(row=1, column=1, pady=(10, 0), sticky="w")

        # Make sure the result_label doesn't expand beyond the frame's size
        self.result_label = ttk.Label(self.main_frame, textvariable=self.result_var,
                                      font=("Helvetica", 14), wraplength=450, width=41)
        self.result_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.score_var = tk.StringVar()
        self.score_var.set("Player: 0 - Computer: 0")
        self.score_label = ttk.Label(self.main_frame, textvariable=self.score_var, font=("Helvetica", 12))
        self.score_label.grid(row=2, column=0, columnspan=3, pady=5)

        # Display images of the choices made by the player and computer
        self.player_image = ttk.Label(self.main_frame, text="Player choice will display here")
        self.computer_image = ttk.Label(self.main_frame, text="Computer choice will display here")
        self.player_image.grid(row=5, column=0, pady=(10, 0))
        self.computer_image.grid(row=5, column=2, pady=(10, 0))

        self.choices = ["Rock", "Paper", "Scissors"]

        for i, choice in enumerate(self.choices):
            btn = ttk.Button(self.main_frame, text=choice, command=lambda c=choice: self.play(c))
            btn.grid(row=3, column=i, padx=5, pady=10)

        self.play_again_btn = ttk.Button(self.main_frame, text="Play again", command=self.reset_game)
        self.play_again_btn.grid(row=4, column=0, columnspan=3, pady=10)
        self.play_again_btn.grid_remove()

        # Load images
        self.images = {}
        for choice in self.choices:
            image = Image.open(f"{choice}.png").resize((100, 100), Image.LANCZOS)
            self.images[choice] = ImageTk.PhotoImage(image)

    def play(self, player_choice):
        total_rounds = self.rounds_var.get()

        if self.current_round < total_rounds:
            self.current_round += 1

            computer_choice = random.choice(self.choices)

            result = self.determine_winner(player_choice, computer_choice)

            if result == "Player":
                self.player_score += 1
                message = f"You win! {player_choice} beats {computer_choice}. We got 'em!"
            elif result == "Computer":
                self.computer_score += 1
                message = f"You lose! {computer_choice} beats {player_choice}. You can do better."
            else:
                message = f"Things just got heated. It's a tie! Both chose {player_choice}."

            self.result_var.set(f"Round {self.current_round}/{total_rounds}: {message}")
            self.score_var.set(f"Player: {self.player_score} - Computer: {self.computer_score}")

            # Update GIFs
            self.set_images(player_choice, computer_choice)

            if self.current_round == total_rounds:
                self.result_var.set(
                    f"Game over! Final score: Player {self.player_score} - Computer {self.computer_score}")
                self.play_again_btn.grid()
        else:
            self.result_var.set("Game over! Click 'Play again' to start a new game.")

    def determine_winner(self, player, computer):
        if player == computer:
            return "Tie"
        elif (
                (player == "Rock" and computer == "Scissors") or
                (player == "Paper" and computer == "Rock") or
                (player == "Scissors" and computer == "Paper")
        ):
            return "Player"
        else:
            return "Computer"

    def set_images(self, player_choice, computer_choice):
        self.player_image.config(image=self.images[player_choice])
        self.computer_image.config(image=self.images[computer_choice])

    def reset_game(self):
        self.result_var.set("Make your choice. The world depends on it.")
        self.play_again_btn.grid_remove()
        self.player_score, self.computer_score, self.current_round = 0, 0, 0
        self.score_var.set(f"Player: {self.player_score} - Computer: {self.computer_score}")
        self.player_image.config(image="")
        self.computer_image.config(image="")


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
