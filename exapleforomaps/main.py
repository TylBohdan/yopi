import math

from sympy import diff, Symbol


def foo1(a, b):
    result = a - foo(a) * (b - a) / (foo(b) - foo(a))
    return result

def foo(x):
    return x**4 - 3 * x**3 - 1 / (1 + x**2) + 4 * x

def df_dx(f, x, h = 1e-7):
    return (f(x + h) - f(x)) / h

#print(foo, 0)
print(foo(0.246))
#print(foo1(0, 0.2460))




