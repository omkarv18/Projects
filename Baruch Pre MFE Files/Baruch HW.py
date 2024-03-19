import numpy as np

values = np.array([1/12, 7/12, 13/12, 19/12])

r_vals = 0.05 + 0.005 * np.sqrt(values + 1)

print(r_vals)

answer = 3.5 * np.exp(-r_vals[:-1] * values[:-1])

print(answer)

answer = np.sum(answer) + 103.5 * np.exp(-r_vals[-1] * values[-1])

print(answer)