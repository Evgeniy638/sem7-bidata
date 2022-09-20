def task1():
    sum = 0
    sum_squares = 0

    while True:
        number = float(input())

        sum += number
        sum_squares += number ** 2

        if sum == 0:
            break

    print(sum_squares)


if __name__ == '__main__':
    task1()
