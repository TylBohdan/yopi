import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def bisection(f, a, b, error_tolerance = 1e-15, max_iterations = 500):
    k = 0
    table = PrettyTable(['Номер ітерації', 'x', 'f(x)', 'Похибка наближення'])
    while k < max_iterations:
        c = (a + b) / 2
        if f(a) * f(c) > 0:
            a = c
        else: b = c
        k = k + 1
        table.add_row([k, (a + b) / 2, f(c), b - a])
        if np.abs(b - a) < error_tolerance:
            print('root found within tolerance', error_tolerance, 'using', k, 'iterations')
            print(table)
            return (a + b) / 2
    raise RuntimeError('no root found within tolerance', error_tolerance, 'using', max_iterations, 'iterations')

def hord(f, a, b, error_tolerance = 1e-15, max_iterations = 500):
    k = 0
    table = PrettyTable(['Номер ітерації', 'x', 'f(x)', 'Похибка наближення'])
    while k < max_iterations:
        c = a - f(a) * (b - a) / (f(b) - f(a))
        if f(a) * f(c) >= 0:
            a = c
        else: b = c
        k = k + 1
        table.add_row([k, (a + b) / 2, f(c), b - a])
        if np.abs(b - a) < error_tolerance:
            print('root found within tolerance', error_tolerance, 'using', k, 'iterations')
            print(table)
            return (a + b) / 2
    raise RuntimeError('no root found within tolerance', error_tolerance, 'using', max_iterations, 'iterations')

def newton(f, a, error_tolerance = 1e-15, max_iterations = 500):
    def df_dx(f, x, h = 1e-7):
        return (f(x + h) - f(x)) / h
    k = 0
    table = PrettyTable(['Номер ітерації', 'x', 'f(x)'])
    while k < max_iterations:
        x = a - f(a) / df_dx(f, a)
        k = k + 1
        table.add_row([k, x, f(x)])
        if np.abs(f(x)) < error_tolerance:
            print('root found within tolerance', error_tolerance, 'using', k, 'iterations')
            print(table)
            return x
        a = x
    raise RuntimeError('no root found within tolerance', error_tolerance, 'using', max_iterations, 'iterations')

def f(x):
    return x**4 - 3 * x**3 - 1 / (1 + x**2) + 4 * x

x = np.linspace(-3, 3, 1000)
root = bisection(f, 0, 1)
print(root)
root1 = hord(f, 0, 1)
print(root1)
root3 = newton(f, 0)
print(root3)
fig, ax = plt.subplots()
ax.plot(x, f(x))
ax.scatter(root, f(root))
ax.axhline(0, color = 'black', linestyle = '--')
plt.show()