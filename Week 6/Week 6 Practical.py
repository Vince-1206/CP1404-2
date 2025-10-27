TEETH_INDEX = 1

monsters = [["Mike", 340, "blue"],
            ["James", 14, "green"],
            ["Randall", 24, "purple"]]

scary_monsters = [monster for monster in monsters if monster[TEETH_INDEX] > 16]

print(scary_monsters)