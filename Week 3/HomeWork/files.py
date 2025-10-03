
# Task 1: Write the user's name to a file
name = input("Enter your name: ")
with open("name.txt", "w") as name_file:
    name_file.write(name)

# Task 2: Read the name from the file and print a greeting
with open("name.txt", "r") as name_file:
    name = name_file.read().strip()
print(f"Hi {name}!")

# Task 3: Add the first two numbers from numbers.txt and print the result
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
result = first_number + second_number
print(f"The sum of the first two numbers is: {result}")

# Task 4: Accumulator pattern using a for-loop
total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:          # repeated task -> for-loop
        total += int(line.strip())      # accumulator
print(f"The total of all numbers is: {total}")
