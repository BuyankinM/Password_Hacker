from itertools import combinations

for i in range(1, 4):
    for bouquet in combinations(flower_names, i):
        print(bouquet)