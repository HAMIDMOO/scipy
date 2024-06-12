import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
y = np.array([1.0, 1.5, 2.1, 2.8, 3.6, 4.5, 5.5, 6.6, 7.8, 9.1])

def power_function(x, a, b, c):
    return a * x**b + c


popt, pcov = curve_fit(power_function, x, y)
a, b, c = popt


y_pred = power_function(x, a, b, c)


plt.plot(x, y, "o", label="data")
plt.plot(x, y_pred, "-", label="fit")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


