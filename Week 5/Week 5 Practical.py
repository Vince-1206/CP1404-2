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

from operator import itemgetter
data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
name_width = max((len(pair[0]) for pair in data))
score_width = max((len(str(pair[1])) for pair in data))


for pair in sorted(data, key=itemgetter(1), reverse=True):
    name, score = pair
    print(f"{name:{name_width}} = {score:{score_width}}")