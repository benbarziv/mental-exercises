import random
import os
import time

def run_letter_value_game():
    letters = 'ABCDEFGH'

    while True:
        os.system('clear')  # Use 'cls' if you're on Windows, 'clear' for Unix/Linux
        random_letter = random.choice(letters)
        print(f"Random Letter: {random_letter}")

        user_input = input("Guess the value of the letter (number 1-8) or type 'exit' to stop: ")
        if user_input.lower() == 'exit':
            print("Exiting the game.")
            break

        letter_value = letters.index(random_letter) + 1

        if user_input.isdigit() and int(user_input) == letter_value:
            print("Correct!")
            continue  # Immediately restart the loop, skipping the delay
        else:
            print(f"Incorrect! The correct value was {letter_value}.")
            time.sleep(3)  # Delay to allow the user to see the correct answer

if __name__ == "__main__":
    run_letter_value_game()
