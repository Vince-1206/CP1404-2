data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

sorted_data = sorted(data, key=lambda item: item[1], reverse=True)

max_len = max(len(name) for name, score in sorted_data)

for name, score in sorted_data:
    print(f"{name:<{max_len}} = {score}")
