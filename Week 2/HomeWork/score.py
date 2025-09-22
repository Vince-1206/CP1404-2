"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""

import random


def main():
    """Ask for a score, print its result, then generate and show a random score result."""
    score = float(input("Enter score: "))
    print(f"Your score result: {get_score_result(score)}")
    random_score = random.randint(0, 100)
    print(f"Random score ({random_score}): {get_score_result(random_score)}")


def get_score_result(score: float) -> str:
    """Return the grade category for a numeric score in [0, 100]; otherwise 'Invalid score'."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


main()