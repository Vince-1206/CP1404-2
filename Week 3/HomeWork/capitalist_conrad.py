"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""

import random

FILENAME = "output.txt"
MAX_INCREASE = 0.10     # 10%
MAX_DECREASE = 0.05     # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
day = 0

with open(FILENAME, "w") as out_file:
    print(f"Starting price: ${price:,.2f}", file=out_file)
    while MIN_PRICE <= price <= MAX_PRICE:
        if random.randint(1, 2) == 1:
            change = random.uniform(0, MAX_INCREASE)
        else:
            change = random.uniform(-MAX_DECREASE, 0)
        price *= (1 + change)
        day += 1
        print(f"On day {day} price is: ${price:,.2f}", file=out_file)
