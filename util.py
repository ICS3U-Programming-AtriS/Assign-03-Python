#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 2, 2025
# This module contains utility functions

# Colors
BLACK = "\033[0;30m"        # Black
RED = "\033[0;31m"          # Red
GREEN = "\033[0;32m"        # Green
YELLOW = "\033[0;33m"       # Yellow
BLUE = "\033[0;34m"         # Blue
PURPLE = "\033[0;35m"       # Purple
CYAN = "\033[0;36m"         # Cyan
WHITE = "\033[0;37m"        # White [DEFAULT]

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
            red(f"Please enter a valid option from the list")

def red(msg: str, newline = True):
    # Error messages will be red
    print(RED, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline == True:
        print()
    # Reset Color back to default
    print(WHITE, end="")

def blue(msg: str, newline = True):
    # We will use blue text when taking input from the user
    print(BLUE, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline == True:
        print()
    # Reset Color back to default
    print(WHITE, end="")

def cyan(msg: str, newline = True):
    # We will use blue text when taking input from the user
    print(CYAN, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline == True:
        print()
    # Reset Color back to default
    print(WHITE, end="")

def purple(msg: str, newline = True):
    # We will use blue text when taking input from the user
    print(PURPLE, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline == True:
        print()
    # Reset Color back to default
    print(WHITE, end="")

def yellow(msg: str, newline = True):
    # We will use blue text when taking input from the user
    print(YELLOW, end="")
    # Print Message
    print(msg, end="")
    # Add newline if newline == True
    if newline == True:
        print()
    # Reset Color back to default
    print(WHITE, end="")

def line_break():
    yellow("#~#~#~#~#~#~#~#~#~#~#")

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
