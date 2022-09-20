def task2():
    N = int(input())

    list = []
    current_num = 1
    count_current_num = 0

    for i in range(N):
        list.append(current_num)
        count_current_num += 1

        if count_current_num == current_num:
            count_current_num = 0
            current_num += 1

    print(*list)


if __name__ == '__main__':
    task2()
