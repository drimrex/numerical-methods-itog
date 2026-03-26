from math import *

def phi(x):
    """Итерационная функция x = (30/7)*sin(8x) + 9/7"""
    return (30/7) * sin(8*x) + 9/7

def fixed_iteration(x0, eps, max_iter=100):
    """
    Метод простой итерации
    x0 - начальное приближение
    eps - требуемая точность
    max_iter - максимальное число итераций
    """
    x = x0
    print(f"{' Итерация ;      '}  {'x_n ;        '}  {'x_(n+1) ;    '}  {'|x_(n+1)-x_n| ;'}")
    print("-" * 65)
    
    for i in range(max_iter + 1):
        x_next = phi(x)
        error = abs(x_next - x)
        print(f"{i} | {x} | {x_next} | {error}")
        
        if error < eps:
            print(f"\nДостигнута точность {eps} за {i+1} итераций")
            return x_next
        x = x_next
    
    print(f"\nМаксимальное число итераций ({max_iter}) достигнуто")
    return x

# Выбираем начальное приближение из интервала [-0.35; -0.3]
x0 = -0.325

print("Метод простой итерации для уравнения: 3sin(8x) = 0.7x - 0.9")
print(f"Начальное приближение: x0 = {x0}")
print(f"Итерационная функция: φ(x) = (30/7)*sin(8x) + 9/7\n")

Answer = fixed_iteration(x0, 10**(-6))

print(f"\nРезультат: x ≈ {Answer}")