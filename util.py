#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 2, 2025
# This module contains utility functions

# TERMINAL COLOR SEQUENCES
RED = "\033[0;31m"  # Red
YELLOW = "\033[0;33m"  # Yellow
BLUE = "\033[0;34m"  # Blue
PURPLE = "\033[0;35m"  # Purple
CYAN = "\033[0;36m"  # Cyan
WHITE = "\033[0;37m"  # White [DEFAULT]


# Function for handling input
def option_input(prompt: str, options: list):
    line_break()
    while True:
        # Display available options
        blue(f"Options: {str(options)}")
        # Display prompt
        cyan(prompt, newline=False)
        choice = input()
        if choice.upper() in options:
            line_break()
            return choice.upper()
        else:
            red("Please enter a valid option from the list")


# print() but it's red
def red(msg: str, newline=True):
    # Set the color
    print(RED, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline:
        print()
    # Reset Color back to default
    print(WHITE, end="")


# print() but it's blue
def blue(msg: str, newline=True):
    # Set the color
    print(BLUE, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline:
        print()
    # Reset Color back to default
    print(WHITE, end="")


# print() but it's cyan
def cyan(msg: str, newline=True):
    # Set the color
    print(CYAN, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline:
        print()
    # Reset Color back to default
    print(WHITE, end="")


# print() but it's purple
def purple(msg: str, newline=True):
    # Set the color
    print(PURPLE, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline:
        print()
    # Reset Color back to default
    print(WHITE, end="")


# print() but it's yellow
def yellow(msg: str, newline=True):
    # Set the color
    print(YELLOW, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline:
        print()
    # Reset Color back to default
    print(WHITE, end="")


# Prints a string that divides the terminal output
def line_break():
    yellow("#~#~#~#~#~#~#~#~#~#~#")


# LIST OF ALL LETTERS
# I could also do [char for char in "ABCD..."]
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
