from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


# x= np.array([0.0, 0.11, 0.22, 0.33, 0.44, 0.55 , 0.66, 0.77, 0.88, 1])
# y= np.array([4.03, 3.27, 5.38, 7.27, 5.11, 5.8, 7.63, 10.48, 11.43, 15 ])

# def f(x, a, b):
#     return 1/( a+ (b*x))

# popt,pcov= curve_fit(f, x, y)
# a,b =popt

# yperd= f(x, a, b)

# plt.plot(x,y, "o", label="data")
# plt.plot(x, yperd, "-", label="fit")
# plt.xlabel('x')
# plt.legend()
# plt.show()








x = np.array([0.0, 0.69, 1.38, 2.07, 2.76, 3.45, 4.14, 4.83, 5.52, 6.21])
y = np.array([0.479, 1.529, 1.970, 1.412, 0.026, -1.425, -1.979, -1.506, -0.483, 1.514])


def sinusoidal_function(x, A, omega, phi):
    return A * np.sin(omega * x + phi)

 
popt, pcov = curve_fit(sinusoidal_function, x, y, maxfev=10000)
A, omega, phi = popt


y_pred = sinusoidal_function(x, A, omega, phi)

# رسم داده‌ها و تابع برازش داده شده
plt.plot(x, y, "o", label="data")
plt.plot(x, y_pred, "-", label="fit")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()








# x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
# y = np.array([1.0, 1.5, 2.1, 2.8, 3.6, 4.5, 5.5, 6.6, 7.8, 9.1])

# def power_function(x, a, b, c):
#     return a * x**b + c


# popt, pcov = curve_fit(power_function, x, y)
# a, b, c = popt


# y_pred = power_function(x, a, b, c)


# plt.plot(x, y, "o", label="data")
# plt.plot(x, y_pred, "-", label="fit")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()