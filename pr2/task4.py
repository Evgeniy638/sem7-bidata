def task4():
    A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    result = {}

    for i, key in enumerate(B):
        if key in result:
            result[key] += A[i]
        else:
            result[key] = A[i]

    print(result)


if __name__ == '__main__':
    task4()
