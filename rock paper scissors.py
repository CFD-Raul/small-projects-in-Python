# importing the random module

import random

# setting the game processes

def rock_paper_scissors():
    # creating the list of options
    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    options = list(beats.keys())

    # obtaining user choice
    user_choice = input("Choose one between 'Rock', 'Paper' or 'Scissors': ").lower()
    # validating user input
    if user_choice not in options:
        print("Invalid option!")
        rock_paper_scissors()
        return
    # generating computer choice
    computer_choice = random.choice(options)
    # generating results
    result = ""
    # game rules
    if user_choice == computer_choice:
        result = "Draw!"
    elif beats[user_choice] == computer_choice:
        result = "You Win!"
    else:
        result = "The Machine Wins!"
    # displaying game results
    message = f"You chose {user_choice}, the Machine chose {computer_choice}, the result is: {result}"
    print(message)

rock_paper_scissors()