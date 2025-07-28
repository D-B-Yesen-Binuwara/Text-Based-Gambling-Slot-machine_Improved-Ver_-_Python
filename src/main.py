import random
import time
import os

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

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = list(symbols.keys())
    weights = list(symbols.values())

    columns = []
    for _ in range(cols):
        column = random.choices(all_symbols, weights=weights, k=rows)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(ROWS):
        for i, column in enumerate(columns):
            end_char = " | " if i != COLS - 1 else "\n"
            print(column[row], end=end_char)

def log_session(text):
    log_path = os.path.join(os.path.dirname(__file__), "slot_game_log.txt")
    with open("slot_game_log.txt", "a") as file:
        file.write(text + "\n")

def deposit():
    amount = get_valid_int("Enter the amount you want to deposit: $", 1)
    print("Amount Deposited Successfully.")
    log_session(f"\n Deposited: ${amount}")
    return amount