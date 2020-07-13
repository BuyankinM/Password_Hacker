from itertools import product

for name, last_name in product(first_names, middle_names):
    print(name, last_name)