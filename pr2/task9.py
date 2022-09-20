from task6 import task6


def task9():
    frame = task6()
    return frame.loc[(frame.HouseAge > 50) & (frame.Population > 2500)]


if __name__ == '__main__':
    print(task9())
