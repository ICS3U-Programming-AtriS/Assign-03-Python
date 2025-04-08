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

    # Loop
    while True:
        # Ask user what game they want to play
        selected_game = util.option_input("What Game do you want to play?: ", game_list)
        
        # effect
        util.line_break()
        # Take the user to the game they want to play
        match selected_game:
            case "RPS":
                rps.main()
            case "COIN":
                coin_flip.main()
            case "NUMBER":
                num_guess.main()
            case "HANGMAN":
                hangman.main()
            case "EXIT":
                util.purple("FACT: 99\u0025 of gamblers quit before they win big!")
                util.purple("Be sure to come back!")
                break
        # effect
        util.line_break()



if __name__ == "__main__":
    main()