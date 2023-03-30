import numpy as np
import scipy.linalg as la


def power_iteration(A, max_it):
    n, n = A.shape
    e_vec = np.random.rand(n)
    for i in range(max_it):
        e_vec_new = A @ e_vec
        e_vec = e_vec_new / la.norm(e_vec_new)
    e_val = la.norm(A @ e_vec)
    print(e_vec, e_val)
    return e_vec, e_val


def inverse_power_iteration(A, max_it):
    n, n = A.shape
    e_vec = np.random.rand(n)
    for i in range(max_it):
        e_vec_new = la.inv(A) @ e_vec
        e_vec = e_vec_new / la.norm(e_vec_new)
    e_val = 1. / la.norm(la.inv(A) @ e_vec)
    return e_vec, e_val


def main():
    # A = np.random.rand(3, 3)
    # e_vec, e_val = power_iteration(A, 50)
    # np.testing.assert_almost_equal(e_val, np.max(np.abs(la.eigvals(A))), decimal=15)

    # A = np.random.rand(3, 3)
    # e_vec, e_val = inverse_power_iteration(A, 50)
    # print(e_vec, e_val)
    # np.testing.assert_almost_equal(e_val, np.min(np.abs(la.eigvals(A))), decimal=15)

    A = np.array([[1., 2, 0], [-1, 2, -1], [0, -1, 2]])
    e_vec, e_val = power_iteration(A, 50)
    print(e_vec, e_val)
    np.testing.assert_almost_equal(e_val, np.max(np.abs(la.eigvals(A))), decimal=15)


if __name__ == '__main__':
    main()