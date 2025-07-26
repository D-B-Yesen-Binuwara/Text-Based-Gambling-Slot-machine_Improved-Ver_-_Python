import random
import time
#import os

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 5000
ROWS = 3
COLS = 3

# Symbol count
symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Symbol match multiplier
symbol_values = {
    "A": 10,
    "B": 8,
    "C": 5,
    "D": 2
}

def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if (min_val is None or value >= min_val) and (max_val is None or value <= max_val):
                return value
            else:
                print(f"Enter a value between {min_val} and {max_val}")
        else:
            print("Must be a number")

