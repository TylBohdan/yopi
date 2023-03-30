import numpy as np
from scipy import linalg
from prettytable import PrettyTable


def get_coefficient_to_floats(coefficient_row):
    return list(map(float, coefficient_row.split()))


def get_coefficients():
    coefficients = []
    while True:
        coefficient_row = input('Enter coefficients of matrix A: ')
        if coefficient_row == '-':
            break
        coefficients.append(get_coefficient_to_floats(coefficient_row))

    coefficient_row = input('Enter coefficients of vector b: ')
    b = np.array(get_coefficient_to_floats(coefficient_row))
    return np.array(coefficients), b

def show_input(a, b):
    print('Input coefficients of matrix A')
    print_array(a)
    print('Input coefficients of vector b')
    print_array(b)

def show_result_vector(x):
    print('Result vector x:')
    print_array(x)

def show_results(a, x, b):
    show_result_vector(x)
    show_result_residual_vector(a, x, b)

def show_result_residual_vector(a, x, b):
    print('Result residual vector r=Ax-b:')
    print_array(a @ x - b)

def print_array(array):
    pretty_table = PrettyTable()
    try:
        for row in array:
            pretty_table.add_row(row)
    except TypeError:
        pretty_table.add_row(array)
    print(pretty_table.get_string(header=False))

def gauss_method(a, b):
    n = len(b)
    for k in range(n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.:
                if a[k, k] == 0:
                    a[k, k] = 1.0e-10
                lam = a[i, k] / a[k, k]
                a[i, k + 1:n] = a[i, k + 1:n] - lam * a[k, k + 1:n]
                b[i] = b[i] - lam * b[k]
    return a, b


def forward_substitution(a, b):
    n, n = a.shape
    x = np.zeros(n)
    for i in range(n):
        if a[i, i] == 0:
            a[i, i] = 1
        x[i] = 1.0 / a[i, i] * (b[i] - a[i, :] @ x)
    return x


def backward_substitution(a, b):
    n, n = a.shape
    x = np.zeros(n)
    for i in reversed(range(n)):
        if a[i, i] == 0:
            a[i, i] = 1.0e-10
        x[i] = 1.0 / a[i, i] * (b[i] - a[i, :] @ x)
    return x


def lu_decomposition(a):
    n, n = a.shape
    lower = np.zeros((n, n))
    upper = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            upper[i, j] = a[i, j] - lower[i, :] @ upper[:, j]
            if upper[i, i] == 0:
                upper[i, i] = 1.0e-10
            lower[j, i] = 1.0 / upper[i, i] * (a[j, i] - lower[j, :] @ upper[:, i])
    return lower, upper



def jacobi_method(
    a, b, error_tolerance, max_iteration_number = 500):
    n, n = a.shape
    x = np.zeros(n)
    x_new = a
    k = 0
    while linalg.norm(np.dot(a, x) - b) > error_tolerance:
        for i in range(n):
            x_new[i] = (1.0 / a[i, i]) * (
                    b[i] - np.dot(a[i, :i], x[:i]) - np.dot(a[i, i+1:], x[i+1:]))
        x = x_new
        k = k + 1
        if max_iteration_number == k:
            raise RuntimeError(
                f'no root found within tolerance {error_tolerance} '
                f'using {max_iteration_number} iterations'
            )
    rounding = 0
    while error_tolerance < 1:
       rounding += 1
       error_tolerance *= 10
    x = np.array([round(_, rounding) for _ in x])
    return x, k



def gauss_seidel_method(
    a, b, error_tolerance, max_iteration_number = 500):
    n, n = a.shape
    x = np.zeros(n)
    k = 0
    while linalg.norm(np.dot(a, x) - b) > error_tolerance:
        for i in range(n):
            x[i] = (1.0 / a[i, i]) * (
                    b[i] - np.dot(a[i, :i], x[:i]) - np.dot(a[i, i+1:], x[i+1:]))
        k = k + 1
        if max_iteration_number == k:
            raise RuntimeError(
                f'no root found within tolerance {error_tolerance} '
                f'using {max_iteration_number} iterations'
            )
    rounding = 0
    while error_tolerance < 1:
       rounding += 1
       error_tolerance *= 10
    x = np.array([round(_, rounding) for _ in x])
    return x, k


def task1():
    a, b = get_coefficients()
    show_input(a, b)

    print('Gauss method:')
    x = backward_substitution(*gauss_method(a.copy(), b.copy()))
    show_results(a, x, b)

    print('LU decomposition method:')
    lower, upper = lu_decomposition(a)
    x = backward_substitution(upper, forward_substitution(lower, b))
    show_results(a, x, b)


def task2():
    a, b = get_coefficients()
    show_input(a, b)

    print('Jacobi method:')
    x, iteration_number = jacobi_method(a, b, 1.0e-10)
    show_results(a, x, b)
    print(f'Iteration number: {iteration_number}')

    print('Gauss Seidel method:')
    x, iteration_number = gauss_seidel_method(a, b, 1.0e-10)
    show_results(a, x, b)
    print(f'Iteration number: {iteration_number}')


if __name__ == '__main__':
    #task1()
    task2()









