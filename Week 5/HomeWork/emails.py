"""
Emails to Names
Estimate: 20 minutes
Actual:
"""

def extract_name_from_email(email):
    """Extract a person's name from their email address."""
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name


def main():
    """Prompt user for emails and map them to names."""
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if not email:
            break

        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation and confirmation != 'y':
            name = input("Name: ").strip().title()

        email_to_name[email] = name

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
