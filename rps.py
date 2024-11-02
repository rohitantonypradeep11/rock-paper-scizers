import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"
    
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# Set up the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create buttons
rock_button = tk.Button(root, text="Rock", command=lambda: determine_winner("Rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: determine_winner("Paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: determine_winner("Scissors"))

# Layout buttons
rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Run the application
root.mainloop()
