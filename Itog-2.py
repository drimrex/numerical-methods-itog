from math import *
def bisection(f, a, b, eps):
    if f(a) * f(b) >= 0:
        return None
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def f(x):
    return 3*sin(8*x) - 0.7*x + 0.9

Answer = bisection(f, -0.4, -0.2, 1e-3)
print(Answer)  # должно выйти ≈ -0.3469