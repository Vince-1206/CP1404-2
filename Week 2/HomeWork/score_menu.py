"""
CP1404/CP5632 - Practical
Score menu program with functions
"""
def get_valid_score():
    """Get a valid score between 0 and 100 (inclusive)."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score

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

def show_stars(score):
    """Print stars equal to the score value."""
    print("*" * int(score))

def main():
    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

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

main()