#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 7, 2025
# Lobby for Casino

import util
import coin_flip
import hangman
import num_guess
import rps


def main():
    # Introduction message
    print("Welcome to THE CASINO!")

    # List of available games
    game_list = ["RPS", "COIN", "NUMBER", "HANGMAN", "EXIT"]

    # Game Selection Loop
    while True:
        # Ask user what game they want to play
        selected_game = util.option_input("What Game do you want to play?: ", game_list)

        # Line Separation Effect
        util.line_break()

        # Take the user to the game they want to play
        match selected_game:
            case "RPS":
                # Rock Paper Scissors
                rps.main()
            case "COIN":
                # Coin Flipping Game
                coin_flip.main()
            case "NUMBER":
                # Number Guessing Game
                num_guess.main()
            case "HANGMAN":
                # Hangman Game
                hangman.main()
            case "EXIT":
                # Provide the user with factual knowledge
                # \u0025 is the unicode sequence for "%"
                util.purple("FACT: 99\u0025 of gamblers quit before they win big!")
                util.purple("Be sure to come back!")
                # Exit loop, consequently ending the program
                break
        # Line Separation Effect
        util.line_break()


if __name__ == "__main__":
    main()
