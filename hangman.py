#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 2, 2025
# HANGMAN GAME

import random
import util


def main():

    # List of 3-letter words
    # Carefully engineered so that no sequence of 5 characters
    # will empty out the list
    word_list = [
        "BAT",
        "BAR",
        "BTW",
        "BAN",
        "BIN",
        "CAR",
        "CAT",
        "CAP",
        "CAN",
        "DOG",
        "FAN",
        "FAT",
        "FIN",
        "FUN",
        "GAP",
        "GUN",
        "HUT",
        "HMM",
        "JET",
        "JOB",
        "JOY",
        "KIT",
        "LOG",
        "MAN",
        "MAP",
        "NAP",
        "NET",
        "PEN",
        "PET",
        "PIN",
        "POT",
        "PRY",
        "RAT",
        "SUN",
        "SPY",
        "SSH",
        "VAN",
        "WIT",
        "WHY",
        "YES",
        "ZAP",
    ]

    # Initialize a list to contain the guessed letters
    guessed_letters = []

    # Guessing Loop
    for i in range(5, 0, -1):
        # Print amount of of lives
        print(f"You have {i} lives left")
        # Shows all previously guessed letters
        print(f"Guessed letters : {" ".join(guessed_letters)}")
        # This message will always stay the same
        print("Word [3 letters left] : _ _ _")

        # Filter out guessed letters from ALPHABET_LIST
        # Basically remaining_options will become a list
        # of every letter except the ones that the user guessed
        remaining_options = [
            letter for letter in util.ALPHABET_LIST if letter not in guessed_letters
        ]

        # Get a letter from the user
        guess = util.option_input("Enter a letter: ", remaining_options)
        # Add the user's guessed letter to the list of guesses
        guessed_letters.append(guess)

        # At the end of every round:
        # Remove all words from the word list,
        # that contain the user's guessed letter
        # [ Loop through all words in the word list ]
        # [:] creates a copy of the list
        # Done this way because the program
        # shouldn't edit the list whilst iterating through it
        for word in word_list[:]:
            # Check if the letter is in the word
            if guess in word:
                # If it is, remove the word
                word_list.remove(word)
        # Tell the user that they guessed wrong
        print("Unfortunately, you guessed wrong! You lose a life!")

    # Tell the user they lost
    util.purple("You ran out of lives!")
    # Use a random word from the surviving word list
    # as the correct word
    util.purple(f"The correct word was {random.choice(word_list)}.")


if __name__ == "__main__":
    main()
