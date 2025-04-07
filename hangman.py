#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 2, 2025
# HANGMAN GAME

import random
import util


def main():

    # make word_list
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

    guessed_letters = []

    # get guess from user
    for i in range(5, 0, -1):
        # Print amount of of lives
        print(f"You have {i} lives left")
        print(f"Guessed letters : {" ".join(guessed_letters)}")
        print(f"Word [3 letters left] : _ _ _")

        # Filter out guessed letters from ALPHABET_LIST
        remaining_options = [
            letter for letter in util.ALPHABET_LIST if letter not in guessed_letters
        ]

        # Get letter
        guess = util.option_input("Enter a letter: ", remaining_options)
        guessed_letters.append(guess)

        # Remove all words containing the guess from the word list
        for word in word_list[:]:
            if guess in word:
                word_list.remove(word)
        print("Unfortunately, you guessed wrong! You lose a life!")

    print(f"The correct word was {random.choice(word_list)}")


if __name__ == "__main__":
    main()
