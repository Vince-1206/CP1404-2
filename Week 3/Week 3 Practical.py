"""

filename = input("Enter the filename")
infile = open(filename, "r")
for line in infile :
    if line.startwith("#"):
        print(line.strip())

infile.close()

"""