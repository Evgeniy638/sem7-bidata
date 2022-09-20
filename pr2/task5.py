from sklearn.datasets import fetch_california_housing
import pandas as pd


def task5():
    df = fetch_california_housing(as_frame=True)
    med_house_val = pd.DataFrame(df.target, columns=df.target_names)
    print(med_house_val)


if __name__ == '__main__':
    task5()
