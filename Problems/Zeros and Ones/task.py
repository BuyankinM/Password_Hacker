import numpy as np

row_col, b = int(input()), int(input())

print(np.ones((row_col, row_col)) if b == 1 else np.zeros((row_col, row_col)))