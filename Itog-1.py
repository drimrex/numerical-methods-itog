import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*np.sin(8*x) - 0.7*x + 0.9

x = np.linspace(-1, 1, 1000)
y = f(x)

plt.plot(x, y)
plt.axhline(y=0, color='k', linestyle='-')
plt.axvline(x=0, color='k', linestyle='-')
plt.grid(True)
plt.title('График f(x) = 3sin(8x) - 0.7x + 0.9')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()