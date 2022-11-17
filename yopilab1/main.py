from functools import reduce
from math import sqrt
from typing import TextIO

from matplotlib import pyplot as plt


def get_sorteddict(dict_):
    return dict(sorted(dict_.items(), key=lambda item: item[1]))

def task1(views: list[int], file: TextIO):
    frequencies = get_sorteddict({value: views.count(value) for value in views})
    row_format = '{:>3} {:>15}'
    file.write('Frequency table:\n')
    file.write('Views   Frequency\n')
    for view, frequency in frequencies.items():
        file.write(f'{row_format.format(view, frequency)}\n')
    file.write('====================\n')

    file.write('Table of cumulative frequencies:\n')
    file.write('Views   Cumulative\n')
    previous = 0
    for key, frequency in frequencies.items():
        file.write(f'{row_format.format(key, frequency + previous)}\n')
        previous += frequency
    file.write('====================\n')

    max_views = max(views)
    for index, views in enumerate(views, 1):
        if max_views == views:
            file.write(f'Most viewed film: {index} - {max_views}\n')


def task2(views: list[int], file: TextIO):
    file.write(f'Mode: {max(views)}\n')

    views = sorted(views)
    half_length = len(views) / 2
    file.write(f'Median: {(views[int(half_length - 0.5)] + views[int(half_length)]) / 2}\n')


def task3(views: list[int], file: TextIO):
    films_views_length = len(views)
    mean = reduce(lambda x, y: x + y, views) / films_views_length
    result = 0
    for views in views:
        result += (views - mean) ** 2
    file.write(f'Dispersion: {result / (films_views_length - 1)}\n')

    file.write(f'Mean square deviation of the distribution: {sqrt(result / (films_views_length - 1))}\n')


def task4(views: list[int]):
    plt.figure(figsize=(15, 6), dpi=80)
    plt.xlabel('Views')
    plt.ylabel('Frequency')
    frequencies = get_sorteddict({value: views.count(value) for value in views})
    plt.bar(list(map(str, frequencies.keys())), frequencies.values())
    plt.savefig('result.jpg')


def main():
    file_name = input('Enter file name: ')
    try:
        with open(file_name) as file:
            views = list(map(int, file.read().splitlines()[1:]))
    except FileNotFoundError:
        print('Enter correct file name')
        return

    with open('result.txt', 'w', encoding='utf-8-sig') as file:
        file.write('Task 1:\n')
        task1(views, file)

        file.write('Task 2:\n')
        task2(views, file)

        file.write('Task 3:\n')
        task3(views, file)

        task4(views)


if __name__ == '__main__':
    main()