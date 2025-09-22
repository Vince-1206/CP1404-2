print("Hello World")
"""My password is Vince0689"""
def get_password():
    password = input("Enter password: ")
    while len(password) < 8:
        print("Password too short! Try again.")
        password = input("Enter password: ")
    return password
def print_asterisks(password):
    print("*" * len(password))
def main():
    password = get_password()
    print_asterisks(password)

main()