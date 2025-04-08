#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 27, 2025
# Random Number Guessing Game With Error handling

import random
import util

def main():
    # Get the user's guess as a string
    util.cyan("Enter a number (0-9): ", False)
    user_input = input()

    try:
        # Convert the user's guess to an integer
        user_num = int(user_input)

        if 0 <= user_num <= 9:
            # Generate a random number between 0 and 9, excluding the user's guess
            correct_num = user_num + random.randint(-user_num, 9-user_num)

            # Tell the user that they guessed wrong
            # Also tell them the correct answer
            util.purple(f"Wrong! The correct answer was {correct_num}.")
        else:
            util.purple("Wrong! Hint: The number is between 0 and 9")

    except ValueError:
        # Tell the user that their input wasn't an integer
        util.red(f"{user_input} is not an integer.")


if __name__ == "__main__":
    main()
