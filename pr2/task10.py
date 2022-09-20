from task6 import task6


def task10():
    frame = task6()
    print("Max: {max}".format(max=max(frame.MedHouseVal)))
    print("Min: {min}".format(min=min(frame.MedHouseVal)))


if __name__ == '__main__':
    task10()
