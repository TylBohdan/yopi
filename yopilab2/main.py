from functools import reduce
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from typing import TextIO


def task1_1(array, file: TextIO):
    q1 = 1 / 4 * (len(array) + 1)
    q1 = int(q1)
    result = array[q1 - 1] + 0.25 * (array[q1] - array[q1 - 1])
    file.write(f'Q1: {result}\n')

def task1_2(array, file: TextIO):
    q3 = 3 / 4 * (len(array) + 1)
    q3 = int(q3)
    result = array[q3 - 1] + 0.75 * (array[q3] - array[q3 - 1])
    file.write(f'Q3: {result}\n')

def task1_3(array, file: TextIO):
    p90 = 0.9 * (len(array) + 1)
    p90 = int(p90)
    k = 90
    result = array[p90 - 1] + k / 100 * (array[p90] - array[p90 - 1])
    file.write(f'P90: {result}\n')

def task1(array, file: TextIO):
    task1_1(array, file)

    task1_2(array, file)

    task1_3(array, file)

def task2(array, file: TextIO):
    mean = reduce(lambda x, y: x + y, array) / len(array)
    file.write(f'Average value: {mean}\n')
    result = 0
    for value in array:
        result += (value - mean) ** 2
    file.write(f'Dispersion: {result / (len(array) - 1)}\n')
    file.write((f'Mean square deviation of the distribution: {sqrt(result / (len(array) - 1))}\n'))
    file.write(f'z_score: {(array[4] - mean) / sqrt(result / (len(array)))}\n')


def task3(array, file: TextIO):
    file.write('y = ax + b\n')
    mean = reduce(lambda x, y: x + y, array) / len(array)
    average = 95
    max = 100
    A = [[max, 1],
         [mean, 1]]
    B = [[max],
         [average]]
    result = np.linalg.solve(A, B)
    file.write(f'{result}\n')
    array1 = []
    for _ in array:
        array1.append(round(_ * result[0][0] + result[1][0], 3))
    file.write(f'{array1}\n')


def task4(array: list[int], file: TextIO):
    array = list(map(str, array))
    min = int(array[0][:-1]) if array[0][:-1] else 0
    max = int(array[-1][:-1]) + 1
    stem_and_leaf_plot = {str(k): [] for k in range(min, max)}
    for i in array:
        stem, leaf = i[:-1], i[-1]
        stem = stem if stem else '0'
        stem_and_leaf_plot[stem].append(leaf)
    output = 'Stem Leaf Plot\n'
    for stem, leafs in stem_and_leaf_plot.items():
        line = f' {stem} | '
        for leaf in leafs:
            line += f'{leaf} '
        output += f'{line}\n'
    file.write(output)

def task5(array):
    q2 = 0.5 * (len(array) + 1)
    q2 = int(q2)
    result_q2 = array[q2 - 1] + 0.5 * (array[q2] - array[q2 - 1])
    q1 = 1 / 4 * (len(array) + 1)
    q1 = int(q1)
    result_q1 = array[q1 - 1] + 0.25 * (array[q1] - array[q1 - 1])
    q3 = 3 / 4 * (len(array) + 1)
    q3 = int(q3)
    result_q3 = array[q3 - 1] + 0.75 * (array[q3] - array[q3 - 1])
    fig, ax = plt.subplots()
    boxes = [{
        "label": "Diagram",
        "whislo": array[0],
        "q1": result_q1,
        "med": result_q2,
        "q3": result_q3,
        "whishi": array[-1],
        "fliers": []
    }]
    ax.bxp(boxes, showfliers=False)
    plt.savefig("result.jpg")

def main() -> None:
    file_name = input("Enter file name: ")
    try:
        with open(file_name) as file:
            array = list(map(int, file.read().splitlines()[1:]))
    except FileNotFoundError:
        print("Enter correct file name")
        return
    array = sorted(array)
    with open("result.txt", "w", encoding="utf-8-sig") as file:
        file.write('Task 1\n')
        task1(array, file)
        file.write('Task 2\n')
        task2(array, file)
        file.write('Task 3\n')
        task3(array, file)
        file.write('Task 4\n')
        task4(array, file)
        file.write('Task 5\n')
        task5(array)

if __name__ == "__main__":
    main()