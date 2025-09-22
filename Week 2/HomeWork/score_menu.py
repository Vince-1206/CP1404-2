"""
CP1404/CP5632 - Practical
Score menu program with functions
"""
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the interactive score menu until the user chooses to quit."""
    print(MENU)
    score = get_valid_score()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {get_score_result(score)}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice, please try again.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using the score menu program!")


def get_valid_score() -> float:
    """Prompt for and return a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def get_score_result(score: float) -> str:
    """Return the grade category for a numeric score in [0, 100]; otherwise 'Invalid score'."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


def show_stars(score: float) -> None:
    """Print stars equal to the integer part of the score value."""
    print("*" * int(score))


main()