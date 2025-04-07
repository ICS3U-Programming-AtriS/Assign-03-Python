#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 2, 2025
# This module contains utility functions


def option_input(prompt: str, options: list):
    while True:
        # Display prompt
        print(f"Options: {str(options)}")
        choice = input(prompt)
        if choice.upper() in options:
            return choice.upper()
        else:
            print(f"Please enter a valid option from the list")


ALPHABET_LIST = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
