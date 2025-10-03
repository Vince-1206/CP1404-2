"""
CP1404/CP5632 Practical
Word Generator + Password Generator
"""

import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

# ------------------- WORD GENERATOR -------------------
def generate_word():
    """Generate a word based on a user-defined format with wildcards."""
    print("\n--- Word Generator ---")
    print("Format guide:")
    print(" c or % = consonant")
    print(" v or # = vowel")
    print(" *      = any letter")
    print(" literal letters (like 're') stay as they are")
    print("Example: %re#l -> could produce 'breaul' or 'greil'\n")

    # Ask user for format OR auto-generate one
    choice = input("Do you want to auto-generate a random format? (y/n): ").lower()
    if choice.startswith("y"):
        length = random.randint(5, 8)
        symbols = "cv"  # can extend to "%#*" if desired
        word_format = "".join(random.choice(symbols) for _ in range(length))
        print(f"Auto-generated format: {word_format}")
    else:
        word_format = input("Enter your word format: ").lower()

    word = ""
    for kind in word_format:
        if kind in ("c", "%"):
            word += random.choice(CONSONANTS)
        elif kind in ("v", "#"):
            word += random.choice(VOWELS)
        elif kind == "*":
            word += random.choice(CONSONANTS + VOWELS)
        else:
            word += kind  # literal char

    print("Generated word:", word)


# ------------------- PASSWORD GENERATOR -------------------
def generate_password():
    """Generate a password that meets chosen requirements."""
    print("\n--- Password Generator ---")

    length = int(input("Password length: "))
    use_upper = input("Include uppercase? (y/n): ").lower().startswith("y")
    use_lower = input("Include lowercase? (y/n): ").lower().startswith("y")
    use_digits = input("Include digits? (y/n): ").lower().startswith("y")
    use_special = input("Include special characters? (y/n): ").lower().startswith("y")

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += SPECIAL_CHARACTERS

    if not characters:
        print("Error: You must select at least one character type.")
        return

    password = []

    # Ensure at least one of each chosen type
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(SPECIAL_CHARACTERS))

    # Fill remaining length
    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    print("Generated password:", "".join(password))


# ------------------- MAIN MENU -------------------
def main():
    while True:
        print("\nChoose an option:")
        print("1. Word Generator")
        print("2. Password Generator")
        print("3. Quit")
        choice = input("> ")

        if choice == "1":
            generate_word()
        elif choice == "2":
            generate_password()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
