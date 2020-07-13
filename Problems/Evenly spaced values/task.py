import numpy as np

start, end, step = int(input()), int(input()), int(input())

print(np.linspace(start, end, step)[-2])