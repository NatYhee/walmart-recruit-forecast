import pandas as pd
from copy import deepcopy


def adding_lag_feats(
    df: pd.DataFrame,
    ts_col: str = "sales",
    num_lags: int = 3,
    groubBy_cols: list = ["Store"],
    sort_cols: list = ["Store", "date"],
):
    df = df.sort_values(by=sort_cols, ascending=True)

    for lag in range(1, num_lags + 1):
        new_col = f"{ts_col}_lag{lag}"
        df[new_col] = df.groupby(groubBy_cols)[ts_col].shift(lag)

    return df


def adding_lag_seasonal_feats(
    df: pd.DataFrame,
    ts_col: str = "sales",
    num_lags: int = 1,
    groubBy_cols: list = ["week", "Store"],
    sort_cols: list = ["week", "Store", "year"],
    sort_cols_output: list = ["Store", "date"],
):
    years = list(df["year"].unique())
    if len(years) == 1:
        print(
            f"There is not enough data to do seasonal features. No modification in dataframe"
        )
        return df

    df = df.sort_values(by=sort_cols, ascending=True)

    # lags = max(num_lags, len(years) - 1)
    for lag in range(1, num_lags + 1):
        new_col = f"{ts_col}_ss_lag{lag}"
        df[new_col] = df.groupby(groubBy_cols)[ts_col].shift(lag)

    df = df.sort_values(by=sort_cols_output, ascending=True)

    return df
