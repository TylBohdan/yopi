from functools import reduce
from math import sqrt

import matplotlib.pyplot as plt


def scatter_plot(x_list: list[float], y_list:[float]):
    plt.scatter(x_list, y_list)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    plt.savefig('result.jpg')

def calculate_covariance(y_list: list[float], x_list: list[float], center_of_gravity: tuple[float, float]):
    return sum(
        map(lambda _: _[0] * _[1], zip(x_list, y_list))
    ) / len(y_list) - center_of_gravity[0] * center_of_gravity[1]

def average_y(y_list):
    return reduce(lambda x, y: x + y, y_list) / len(y_list)

def average_x(x_list):
    return reduce(lambda x, y: x + y, x_list) / len(x_list)

def calculate_center_of_gravity(y_list, x_list):
    return average_y(y_list), average_x(x_list)

def calculate_correlation(y_list, x_list, mean_y, mean_x, covariance):
    x_average_square_deviation = average_square_deviation(x_list, mean_x)
    y_average_square_deviation = average_square_deviation(y_list, mean_y)
    return covariance / (x_average_square_deviation * y_average_square_deviation)

def calculate_dispersion(list_, mean_):
    result = 0
    for value in list_:
        result += (value - mean_) ** 2

    return result / len(list_)

def average_square_deviation(list_, mean_):
    return sqrt(calculate_dispersion(list_, mean_))


def task1(y_list: list[float], x_list: list[float], correlation: float):
    scatter_plot(x_list, y_list)
    trend = correlation
    if trend > 0:
        return 'Trend is positive'
    elif trend < 0:
        return 'Trend is negative'
    else: return 'There is no trend'


def task2(y_list: list[float], x_list: list[float]):
    center_of_gravity = calculate_center_of_gravity(y_list, x_list)
    return center_of_gravity, calculate_covariance(x_list, y_list, center_of_gravity)

def task3(x_list, mean_y, mean_x, covariance):
    dispersion = calculate_dispersion(x_list, mean_x)
    first_coefficient = covariance / dispersion
    second_coefficient = mean_y - first_coefficient * mean_x
    return f'y = {first_coefficient}x + {second_coefficient}'

def task4(y_list: list[float], x_list: list[float], mean_y, mean_x, covariance):
    return calculate_correlation(y_list, x_list, mean_y, mean_x, covariance)

def main():
    # file_name = input('Enter file name: ')
    # try:
    #     with open(file_name) as file:
    #         list = list(map(float, file.read().splitlines()[1:]))
    #         for _ in list:
    #             if _ == ' ':
    #
    #
    #
    #         y_and_x_list = list.replace(',', '.').splitlines()[1:]
    #         y_and_x_list = [value.split("\t") for value in y_and_x_list]
    #         y_and_x_new_list = []
    #         y_list = [float(list_[0]) for list_ in y_and_x_list]
    #         x_list = [float(list_[1]) for list_ in y_and_x_list]
    #         y_and_x_new_list.append(y_list)
    #         y_and_x_new_list.append(x_list)
    # except FileNotFoundError:
    #     print('Enter correct file name')
    #     return


    file_name = input('Enter file name: ')
    try:
        with open(file_name) as file:
            y_and_x_list = file.read().replace(',', '.').splitlines()[1:]
            y_and_x_list = [value.split("\t") for value in y_and_x_list]
            y_list = [float(list_[0]) for list_ in y_and_x_list]
            x_list = [float(list_[1]) for list_ in y_and_x_list]
    except FileNotFoundError:
        print('Enter correct file name')
        return


    center_of_gravity, covariance = task2(y_list, x_list)
    correlation = task4(y_list, x_list, center_of_gravity[0], center_of_gravity[1], covariance)
    trend = task1(y_list, x_list, correlation)
    result = task3(x_list, center_of_gravity[0], center_of_gravity[1], covariance)

    output = 'Task 1\n'
    output += f'{trend}\n'
    output += 'Task 2\n'
    output += f'Center of gravity = {center_of_gravity}\nCovariance = {covariance}\n'
    output += 'Task 3\n'
    output += f'Equation {result}\n'
    output += 'Task 4\n'
    output += f'Correlation = {correlation}'

    with open('result.txt', 'w', encoding='utf-8-sig') as file:
        file.write(output)

if __name__ == '__main__':
    main()