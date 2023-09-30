import random

MAX_LINES = 3
MAX_BET = 200
MIN_BET = 1

ROWS = 3
COLS = 3

# how many symbols we want?
symbol_count = {
    "🍎": 2,
    "🍐": 4,
    "🍉": 6,
    "🍌": 8
}

# how value for each symbol
symbol_values = {
    "🍎": 5,
    "🍐": 4,
    "🍉": 3,
    "🍌": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # create a copy of all_symbols list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" ⎮ ")
            else:
                print(column[row], end="")
        print()

# collect users deposit amounts
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        # check if the amount digited is a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount

# collect the users bets 
def get_number_of_lines():
    while True:
        lines = input(
            "How many lines would you like to bet on? (1-" + str(MAX_LINES) + ")? ")
    # check if the amount of lines digited is a number
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

# amount of the bets
def get_bet():
    while True:
        bet_amount = input("What bet would you like to place on each line? $")
        # check if the amount digited is a number
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(
                    f"Amount must be between ${str(MIN_BET)} and ${str(MAX_BET)}")
        else:
            print("Please enter a number")
    return bet_amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet_amount = get_bet()
        total_bet = bet_amount * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(
        f"You are betting ${bet_amount} on {lines} lines. Total bet is equal to ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(
        slots, lines, bet_amount, symbol_values)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        if balance == 0:
            print(
                f"You have lost all your money. Please quit this game (press: q) and try again.")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
