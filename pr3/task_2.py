import numpy as np
from task_1 import task_1, get_population_2020, get_population_russia


def task_2(data_frame):
    # инфорамация о фрейме
    print(data_frame.info())
    # первые 5 строчек
    print(data_frame.head())
    print("кол-во пустых строчек")
    print(data_frame.isna().sum())

    # удаляем все строчки с пустыми значениями
    not_empty_rows, _ = np.where(data_frame.isna())
    data_frame = data_frame.drop(not_empty_rows)
    print(data_frame.isna().sum())

    return data_frame


def get_population_2020_with_task2():
    data_frame = task_2(task_1())

    # получаем популяцию за 2020
    data_frame = get_population_2020(data_frame)

    # берём 30 самых больших
    data_frame = data_frame.sort_values(by='Population', ascending=False).head(30)
    return data_frame


def get_population_russia_with_task2():
    return get_population_russia(task_2(task_1()))


if __name__ == '__main__':
    world_population = task_1()
    world_population = task_2(world_population)


