from scipy import integrate
import numpy as np

def f(x):
    return np.cos(x)**2 * np.sin(x)


I= integrate.quad(f, 0, np.pi/2)
print(I)




def g(x):
    return x* np.exp(2*x)

J= integrate.quad(g, 0, 1)


print(J)




def z(x):
    return np.log10(x)/ x

K= integrate.quad(z, 2, 3)


print(K)