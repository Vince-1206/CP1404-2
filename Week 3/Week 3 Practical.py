"""

filename = input("Enter the filename")
infile = open(filename, "r")
for line in infile :
    if line.startwith("#"):
        print(line.strip())

infile.close()

"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
 