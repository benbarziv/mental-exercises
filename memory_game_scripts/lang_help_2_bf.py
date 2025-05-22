import random
import string
import os
import time

def run_alphabet_exercise():
    alphabet = string.ascii_uppercase
    while True:
        os.system('clear')
        random_letter = random.choice(alphabet)
        print(f"Random Letter: {random_letter}")

        user_input = input("Enter the letter before it (or type 'exit' to stop): ")
        if user_input.lower() == 'exit':
            print("Exiting the exercise.")
            break
        
        before_index = alphabet.index(random_letter) - 1
        after_index = alphabet.index(random_letter) + 1
        
        before_letter = alphabet[before_index] if before_index >= 0 else "None"
        after_letter = alphabet[after_index] if after_index < len(alphabet) else "None"
        
        if user_input.upper() == f"{before_letter}":
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer was {before_letter}.")
            time.sleep(3)

if __name__ == "__main__":
    run_alphabet_exercise()
