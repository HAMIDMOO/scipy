import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def f(t, y):

    return 10*t

v0=1

t= np.linspace(0,5, 40)

y= odeint(f, v0, t)
plt.plot(t,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

