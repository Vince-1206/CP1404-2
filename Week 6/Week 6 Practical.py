
"""
TEETH_INDEX = 1

monsters = [["Mike", 340, "blue"],
            ["James", 14, "green"],
            ["Randall", 24, "purple"]]

scary_monsters = [monster for monster in monsters if monster[TEETH_INDEX] > 16]

print(scary_monsters)

"""
"""
class Monster:
    def __int__ (self, name, scariness, color):
        self.name = name
        self.scariness = scariness
        self.color = color

    def is_scary(self):
        return self.scariness > 100  # You can adjust this threshold

monsters = [
    Monster("Mike", 340, "blue"),
    Monster("James", 14, "green"),
    Monster("Randall", 24, "purple")
]

scary_monsters = [monster for monster in monsters if monster.is_scary()]

for m in scary_monsters:
    print(m.name)

"""


