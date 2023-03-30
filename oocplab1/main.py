import time


def Fib(func):
    def init(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        finish = time.time()
        speed_of_function = finish - begin
        print(speed_of_function)
    return init


@Fib
def fib_rec(value):
    if value == 1:
        return 0
    elif value == 2:
        return 1
    return fib_rec(value - 1) + fib_rec(value - 2)


@Fib
def iteration(value):
    x_0 = 0
    x_1 = 1
    if value == 1:
        return 0
    elif value == 2:
        return 1
    else:
        for _ in range(value - 2):
            x_2 = x_0 + x_1
            x_0 = x_1
            x_1 = x_2
        return(x_2)



if __name__ == '__main__':
    fib_rec(10)
    iteration(10)
