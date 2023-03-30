from math import sin, cos

import numpy as np
from prettytable import PrettyTable

def newton(f_0, f_1, x_0, y_0, error_tolerance = 1e-15, max_iterations = 500):
    def j(x, y):
        return [[cos(x - 0.6), -1], [3, sin(y)]]


    # def j(x, y):
    #     return [[x, -y], [x * (2 * y + x), 1]]







    # def j(x, y):
    #     return [[2 * x, 2 * y], [y, x]]
    def f(x,y):
        return [f_0(x, y), f_1(x, y)]
    k = 0
    table = PrettyTable(['Номер ітерації', 'x_0', 'y_0', "f_0(x_0, y_0), f_1(x_0, y_0)", "Матриця Якобіана", "tolerance"])
    while k < max_iterations:
        j_f = j(x_0, y_0)
        f_x = f(x_0, y_0)
        try:
            delta = np.linalg.solve(j_f, np.array(f_x) * -1)
        except np.linalg.LinAlgError:
            return None
        x_0 += delta[0]
        y_0 += delta[1]
        e = [f_0(x_0, y_0), f_1(x_0, y_0)]
        table.add_row([k, x_0, y_0, f_x, j_f, e])
        k = k + 1
        if f_0(x_0, y_0) < error_tolerance:
            if f_1(x_0, y_0) < error_tolerance:
                print('root found within tolerance', error_tolerance, 'using', k, 'iterations')
                print(table)
                return x_0, y_0
    raise RuntimeError('no root found within tolerance', error_tolerance, 'using', max_iterations, 'iterations')

def f_0(x, y):
    return sin(x - 0.6) - y - 1.6

def f_1(x, y):
    return 3 * x - cos(y) - 0.9



# def f_0(x, y):
#     return x * y - y ** 2 - 1
#
# def f_1(x, y):
#     return (x ** 2) * y + y - 5













# def f_0(x, y):
#     return x**2 + y**2 - 3


# def f_1(x, y):
#     return x * y - 1



root = newton(f_0, f_1, 1.5, 0.5)
print(root)