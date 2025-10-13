data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]


max_len = max(len(name) for name, score in data)

for name, score in data:
    print(f"{name:<{max_len}} = {score}")
