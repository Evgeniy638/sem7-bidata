import numpy as np
from task6 import task6


def task11():
    return task6().apply(np.mean)


if __name__ == '__main__':
    print(task11())
