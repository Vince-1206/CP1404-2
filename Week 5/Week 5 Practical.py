# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
#
# name_width = max((len(pair[0]) for pair in data))
# score_width = max((len(str(pair[1])) for pair in data))
#
# print(name_width)
# print(score_width)
#
# for pair in data:
#     name, score = pair
#     print(f"{name:{name_width}} = {score:{score_width}}")
"""
from operator import itemgetter
data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
name_width = max((len(pair[0]) for pair in data))
score_width = max((len(str(pair[1])) for pair in data))


for pair in sorted(data, key=itemgetter(1), reverse=True):
    name, score = pair
    print(f"{name:{name_width}} = {score:{score_width}}")

"""

"""
name_and_age = {"Bill": 21, "Jane": 34, "Sven": 56}
print(name_and_age)
print(name_and_age["Jane"])
print(len(name_and_age))

name_and_age["Lukas"] = 20
print(name_and_age)

name_and_age["Lukas"] = "ten"
print(name_and_age)

del name_and_age["Lukas"]
print(name_and_age)

print(name_and_age.pop("Bill"))
print(name_and_age)

name_and_age["Jane"] = name_and_age["Sven"]
print(name_and_age)

for name in name_and_age:
    print(name, name_and_age[name])

for i in range(len(name_and_age)):
    print(i)
    
"""

"""
name_and_age = {"Bill": 21, "Jane": 34, "Sven": 56}
print(name_and_age.keys())
print(name_and_age.values())
print(name_and_age.items())

print(max(name_and_age.values()))

for key in name_and_age:
    print(key)

for key in name_and_age:
    print(f"{key} is {name_and_age[key]}")

for key, value in name_and_age.items():
    if value > 50:
        print(key, value)

for name, age in name_and_age.items():
    print(f"{name} is {age}")
    
for name, age in name_and_age.items():
    if age == max(name_and_age.values()):
        print(f"{name} is {age}")

print(list(name_and_age.keys()))
print(name)

"""

"""
name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}

print(name_to_age)

name = input("Enter name:")
age = int(input("Enter age:"))

name_to_age[name] = age

print(name_to_age)
"""

"""
word_to_count = {"apple": 8, "Kiwi": 4}
words = ["apple", "orange"]

for word in words:
    if word in word_to_count:
        word_to_count[word] = word_to_count[word] + 1
        print(word,word_to_count[word])
    else:
        word_to_count[word] = 1
        print(word, word_to_count[word])
"""

"""
my_subjects = {"CP1401", "CP1404", "MA1000"}
your_subjects = {"CP1401", "MN1010", "MA1008"}

print(f"{'union' : 21} :", my_subjects | your_subjects)
print(f"{'difference' :21} : ", my_subjects - your_subjects)
print(f"{'Intersection' :21} :", my_subjects & your_subjects)
print(f"{'Symmetric difference' :21} :", my_subjects ^ your_subjects)
"""

def string_lengths(strings):
    lengths = {}
    for word in strings:
        lengths[word] = len(word)
    return lengths

words = ["Youtube", "VINCE", "Bottle"]
result = string_lengths(words)
print(result)

