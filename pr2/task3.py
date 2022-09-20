import numpy as np


def task3():
    args = list(map(int, input().strip().split()))
    matrix = np.random.rand(args[0], args[1])
    result = []

    for row in matrix:
        for cell in row:
            result.append(cell)

    print("original")
    print(matrix)
    print("result")
    print(result)


if __name__ == '__main__':
    task3()
