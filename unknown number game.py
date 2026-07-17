# importing random module

import random

# creating the number guessing game function

def unknown_number_game():
    # generating secret number
    unknown_number = random.randint(1, 100)
    # attempt counter
    users_attempts = 0
    # establishing the infinite loop
    while True:
        try:
            user_attempt = int(input("Enter an integer between 1 and 100: "))

            if not 1 <= user_attempt <= 100:
                raise ValueError(f"Your guess, {user_attempt}, is not within the pre-established range of 1 to 100. Please try again!")
            
            users_attempts += 1

            if user_attempt < unknown_number:
                print("That's a very low guess, try again with a higher number!")
            elif user_attempt > unknown_number:
                print("That's a very high guess, try again with a lower number!")
            else:
                print(f"Congratulations! You guessed the unknown number {unknown_number}, with {users_attempts} attempts!")
                break
            
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Invalid input! Please enter only integer numbers.")
            else:
                print(f"Invalid input! {e}")         
             
unknown_number_game()