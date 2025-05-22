import random
import os
import time

def run_alphabet_exercise():
    alphabet = 'ABCDEFGHI'  # Limiting to the first 10 letters of the alphabet
    while True:
        os.system('clear')  # Use 'cls' if you're on Windows, 'clear' for Unix/Linux
        random_letter = random.choice(alphabet)
        print(f"Random Letter: {random_letter}")

        user_input = input("Enter the letter before it (or type 'exit' to stop): ")
        if user_input.lower() == 'exit':
            print("Exiting the exercise.")
            break

        before_index = alphabet.index(random_letter) - 1
        
        before_letter = alphabet[before_index] if before_index >= 0 else "0"
        
        if user_input.upper() == before_letter:
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer was {before_letter}.")
            time.sleep(3)  # Giving time to see the answer before the next iteration

if __name__ == "__main__":
    run_alphabet_exercise()
