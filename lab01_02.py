import math

def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

def func1(x):
    return (1 + x + (x ** 2) / fac(2) + (x ** 3) / fac(3) + (x ** 4) / fac(4))

def func2(x):
    return (x * (math.sin( x ** 3) + (math.cos(y) ** 2)))

x = float(input("Введите значение числа х: "))
y = float(input("Введите значение числа y: "))
s = func1(x)
psi = func2(x)
print("Результат вычеслений первой функции равен ", s)
print("Результат вычесления второй функции равен ", psi)
exit()
