import numpy as np
import pandas as pd

A = np.array([
    [1, -4, 3, -1],
    [1,  2, 5, -1],
    [2, -3, 0,  4],
    [-1, -2, -3, -4]
])

b_base = np.array([0, 2, 5, -5])

results = {}

for a in range(-30, 31):
    b = b_base.copy()
    b[0] = a 
    try:
        x = np.linalg.solve(A, b)
        results[a] = x
    except np.linalg.LinAlgError:
        results[a] = [np.nan, np.nan, np.nan, np.nan]

df = pd.DataFrame.from_dict(results, orient='index', columns=['x1', 'x2', 'x3', 'x4'])
print(df)
