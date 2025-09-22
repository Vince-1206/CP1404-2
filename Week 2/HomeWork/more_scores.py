"""
CP1404 - Practical
Lin Han-Wei

"""

import random


def main():
    """Ask for number of scores, generate random scores, and write results to a file."""
    number_of_scores = int(input("How many scores? "))

    with open("results.txt", "w") as out_file:
        for _ in range(number_of_scores):
            score = random.randint(0, 100)
            result = get_score_result(score)
            print(f"{score} is {result}", file=out_file)


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
