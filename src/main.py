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

jackpot_triggered = False
session_turns = 0
session_winnings = 0

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

def check_winnings(columns, lines, bet, values):
    global jackpot_triggered
    winnings = 0
    winning_lines = []
    line_details = []

    for line in range(lines):
        symbol = columns[0][line]
        if all(column[line] == symbol for column in columns):
            win_amount = values[symbol] * bet
            winnings += win_amount
            winning_lines.append(line + 1)
            line_details.append((line + 1, symbol, win_amount))

            if symbol == "A" and COLS >= 3:
                jackpot_triggered = True  # Trigger difficulty increase

    return winnings, winning_lines, line_details

def spin_game(balance):
    global session_turns, session_winnings, jackpot_triggered
    lines = get_valid_int(f"Enter number of lines to bet on (1-{MAX_LINES}): ", 1, MAX_LINES)

    while True:
        bet = get_valid_int("Enter your bet per line: $", MIN_BET, MAX_BET)
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough balance. You have: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet = ${total_bet}")
    log_session(f"\n--- Turn {session_turns + 1} ---")
    log_session(f"Bet: ${bet} x {lines} lines = ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)

    # Log spin result
    spin_result = "\n".join([" | ".join([column[row] for column in slots]) for row in range(ROWS)])
    log_session("Spin result:\n" + spin_result)

    winnings, winning_lines, line_details = check_winnings(slots, lines, bet, symbol_values)

    print(f"You won: ${winnings}")
    for line, symbol, amount in line_details:
        print(f"Line {line} matched '{symbol}' – You won ${amount}")
        log_session(f"Line {line}: '{symbol}' – ${amount} win")

    if winning_lines:
        print("Winning lines:", *winning_lines)
    else:
        print("No matching lines")

    log_session(f"Total winnings this turn: ${winnings}")
    session_turns += 1
    session_winnings += winnings

    if jackpot_triggered:
        #adjust_difficulty_after_jackpot()
        jackpot_triggered = False

    return winnings - total_bet

