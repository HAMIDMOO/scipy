import numpy as np
from scipy.optimize import minimize


def f(x):
    return x + np.exp(-x)

x0 = 0.0


result = minimize(f, x0)

min_point = result.x
min_value = result.fun

print(min_point, min_value)