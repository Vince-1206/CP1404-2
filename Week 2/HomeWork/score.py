"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""

import random

def get_score_result(score):
    """Return the grade category based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
def main():
    score = float(input("Enter score: "))
    print(f"Your score result: {get_score_result(score)}")
    random_score = random.randint(0, 100)
    print(f"Random score ({random_score}): {get_score_result(random_score)}")

main()