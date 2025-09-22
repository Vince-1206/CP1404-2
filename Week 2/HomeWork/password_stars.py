"""
CP1404 - Practical
Lin Han-Wei

"""
print("Hello World")
"""My password is Vince0689"""
MIN_PASSWORD_LENGTH = 8


def main():
    """Prompt for a valid password then print the password as stars."""
    password = get_password(min_length=MIN_PASSWORD_LENGTH)
    print_asterisks(password)


def get_password(min_length: int) -> str:
    """Prompt until a password of at least min_length characters is entered, then return it."""
    password = input(f"Enter password (min {min_length} chars): ")
    while len(password) < min_length:
        print("Password too short! Try again.")
        password = input(f"Enter password (min {min_length} chars): ")
    return password


def print_asterisks(password: str) -> None:
    """Print asterisks matching the length of the given password (no password revealed)."""
    print("*" * len(password))

main()