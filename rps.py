#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 7, 2025
# Rock Paper Scissors

import random
import util


def main():
    # Display Introduction Message
    print(
        """Welcome to rock paper scissors.
Rock beats paper,
paper beats scissors,
and scissors beats rock.
You will be playing Barbable
from Liechtenstein!
First to 3 points wins!"""
    )
    # Initialize user points
    user_points = 0
    # Initialize program points
    program_points = 0
    # Initialize list for choices
    choices = ["ROCK", "PAPER", "SCISSORS"]
    # Game Loop for rounds
    while True:
        # Initialize user_pick as a string value
        user_pick = ""
        # Initialize program_pick as a string value
        program_pick = ""
        # Check if user is 1 point away from winning
        if user_points >= 2:
            # Get user's pick
            user_pick = util.option_input("Rock/Paper/Scissors? ", choices)

            # Set Program pick such that it always results in either
            # a draw or a loss
            if user_pick == "ROCK":
                # program pick is now either "ROCK" or "PAPER"
                program_pick = random.choice(["ROCK", "PAPER"])
            elif user_pick == "PAPER":
                # program pick is now either "PAPER" or "SCISSORS"
                program_pick = random.choice(["PAPER", "SCISSORS"])
            # If it's not ROCK or PAPER, it must be SCISSORS
            else:
                # program pick is now either "SCISSORS" or "ROCK"
                program_pick = random.choice(["SCISSORS", "ROCK"])
        else:
            # Get user's pick
            user_pick = util.option_input("Rock/Paper/Scissors? ", choices)
            # Select a random pick for the program
            program_pick = random.choice(choices)

        # Evaluate the result of the round
        # and award points
        match user_pick:
            case "ROCK":
                # Rock draws with Rock
                if program_pick == "ROCK":
                    print("DRAW!")
                # Rock loses to Paper
                elif program_pick == "PAPER":
                    print("LOSS!")
                    program_points += 1
                # If it's not ROCK or PAPER, it must be SCISSORS
                # Rock beats scissors
                else:
                    print("WIN!")
                    user_points += 1
            case "PAPER":
                # Paper beats Rock
                if program_pick == "ROCK":
                    print("WIN!")
                    user_points += 1
                # Paper draws with Paper
                elif program_pick == "PAPER":
                    print("DRAW!")
                # If it's not ROCK or PAPER, it must be SCISSORS
                # Paper loses to Scissors
                else:
                    print("LOSS!")
                    program_points += 1
            case "SCISSORS":
                # Scissors loses to Rock
                if program_pick == "ROCK":
                    print("LOSS!")
                    program_points += 1
                # Scissors beats Paper
                elif program_pick == "PAPER":
                    print("WIN!")
                    user_points += 1
                # If it's not ROCK or PAPER, it must be SCISSORS
                # Scissors draws with Scissors
                else:
                    print("DRAW!")
        # End the game once program reaches 3 points
        if program_points >= 3:
            util.purple("You lost the set!")
            util.purple("Barbable spits in your face!")
            break

        # Display the score
        # at the end of every round
        print(f"Your points: {user_points}")
        print(f"Barbable's points: {program_points}")


if __name__ == "__main__":
    main()
