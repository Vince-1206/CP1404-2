"""
import random

# Ask user for input
low = int(input("Enter a low number: "))
high = int(input("Enter a high number: "))

# Ensure high > low
while high <= low:
    print("High number must be greater than low number!")
    high = int(input("Enter a high number: "))

# Generate random number between low and high
n = random.randint(low, high)

# Print n smiley faces
print(":)" * n)

"""

def is_even(number):
    """Return True if number is even, False otherwise."""
    return number % 2 == 0


def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))

    # Check if it is even or odd using our function
    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
main()
