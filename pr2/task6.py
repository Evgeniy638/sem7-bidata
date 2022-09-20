from sklearn.datasets import fetch_california_housing
import pandas as pd


def task6():
    df = fetch_california_housing(as_frame=True)
    data = pd.DataFrame(df.data, columns=df.feature_names)
    med_house_val = pd.DataFrame(df.target, columns=df.target_names)
    result = pd.concat([data, med_house_val], axis=1)
    return result


if __name__ == '__main__':
    print(task6())
