import matplotlib.pyplot as plt
from task_2 import get_population_2020_with_task2


def task_6(world_population):
    fig, ax = plt.subplots()
    ax.boxplot(world_population['Population'])

    # предыдущие настройки
    fig.suptitle('Диаграмма популяции стран в 2020', fontsize=20)
    plt.xlabel('Страны', fontsize=16)
    plt.ylabel('Популяция', fontsize=16)

    plt.show()


if __name__ == '__main__':
    task_6(get_population_2020_with_task2())
