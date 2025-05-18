import random
import os
import time

def run_letter_difference_game():
    letters = 'ABCDEFGH'

    while True:
        os.system('clear')  # Use 'cls' if you're on Windows, 'clear' for Unix/Linux
        random_letter1 = random.choice(letters)
        random_letter2 = random.choice(letters)
        print(f"Random Letters: {random_letter1}, {random_letter2}")

        user_input = input("Guess the difference of the letters or type 'exit' to stop: ")
        if user_input.lower() == 'exit':
            print("Exiting the game.")
            break

        letter_value1 = letters.index(random_letter1) + 1
        letter_value2 = letters.index(random_letter2) + 1

        # Calculate the difference by explicitly subtracting the smaller from the larger
        if letter_value1 > letter_value2:
            difference_of_values = letter_value1 - letter_value2
        else:
            difference_of_values = letter_value2 - letter_value1

        if user_input.isdigit() and int(user_input) == difference_of_values:
            print("Correct!")
            continue  # Immediately restart the loop, skipping the delay
        else:
            print(f"Incorrect! The correct difference was {difference_of_values}.")
            time.sleep(3)  # Delay to allow the user to see the correct answer

if __name__ == "__main__":
    run_letter_difference_game()
