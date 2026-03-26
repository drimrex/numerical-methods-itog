from math import *
def n(f1, f2, x0, eps, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f1(x)
        dfx = f2(x)
        x_new = x - fx/dfx
        if abs(x_new - x) < eps:
            return x_new
        x = x_new
    return x

def f1(x):
    return 3*sin(8*x) - 0.7*x + 0.9

def f2(x):
    return 24*cos(8*x) - 0.7

Answer = n(f1, f2, -0.35, 10**(-6))
print(Answer)  # ≈ -0.346721