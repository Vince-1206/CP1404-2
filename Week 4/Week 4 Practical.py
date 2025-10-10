"""
# List of names
names = ["Ada", "Alan", "Bill", "John"]

print("Current names:", ", ".join(names))


while True:
    name_to_remove = input("Who do you want to remove? (Press Enter to stop) ").strip()

    if name_to_remove == "":
        break

    if name_to_remove in names:
        names.remove(name_to_remove)
        print(f"{name_to_remove} removed.")
    else:
        print(f"{name_to_remove} is not in the list.")

    print("Current names:", ", ".join(names))

print("\nFinal list of names:", ", ".join(names))

"""
"""
values = [1, 2, 3, 2]
values.remove(2)
print(values)
"""
"""
before = [1, 4, 0, -1]
after = before.sort()
print(after[0])
"""

"""
words = ["aye", "bee", "sea"]
print("/".join(words))
"""

words = ["aye", "bee", "sea", "bee"]
words.remove("bee")
print(words.pop())