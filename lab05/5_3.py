import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.exp(-x - 1/2)

x = np.linspace(1, 4, 100)

y = [f(i) for i in x]

plt.plot(x, y, label="e^(-x-1/2)")

def df(x):
    return -math.exp(-x - 1/2)

tangent_slope = df(2.3)

tangent = [f(2.3) + tangent_slope*(i - 2.3) for i in x]

plt.plot(x, tangent, label="kasatelnaya x=2.3")
plt.plot(2.3, 0.061, "ro")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()

