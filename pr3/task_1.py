import pandas as pd


def task_1():
    return pd.read_csv('../Countries_Population_from_1995_to_2020.csv')


def get_population_2020(world_population):
    return world_population.loc[world_population.Year == 2020]


def get_population_russia(world_population):
    return world_population.loc[world_population.Country == 'Russia']


if __name__ == '__main__':
    print(task_1().head())
