data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

# Find the longest name length (for alignment)
max_len = max(len(name) for name, score in data)

# Print each name and score neatly aligned
for name, score in data:
    print(f"{name:<{max_len}} = {score}")
