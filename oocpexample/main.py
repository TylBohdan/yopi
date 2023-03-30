def fib_rec(serial: int):
    if serial == 1:
        return 0
    elif serial == 2:
        return 1
    return fib_rec(serial - 1) + fib_rec(serial - 2)

def iteration(serial: int):
    x_0 = 0
    x_1 = 1
    if serial == 1:
        return 0
    elif serial == 2:
        return 1
    else:
        for _ in range(serial - 2):
            x_2 = x_0 + x_1
            x_0 = x_1
            x_1 = x_2
        return(x_2)

print(iteration(10))