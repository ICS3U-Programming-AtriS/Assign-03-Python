#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 7, 2025
# Coin Flipping game

import util


def main():
    # Get user's guess for whether a coin will result in
    # "HEADS" or "TAILS"
    guess = util.option_input("Heads/Tails? ", ["HEADS", "TAILS"])

    if guess == "HEADS":
        # If the user guessed "HEADS", the result is "TAILS"
        util.purple("The coin was tails, unfortunately.")
    # If guess is not "HEADS", it must be "TAILS"
    else:
        # If the user guessed "TAILS", the result is "HEADS"
        util.purple("The coin was heads, unfortunately.")


if __name__ == "__main__":
    main()
