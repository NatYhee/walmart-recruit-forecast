import pandas as pd


def date_setting(df: pd.DataFrame, date_col: str = "Date"):
    df[date_col] = pd.to_datetime(df[date_col])
    df["week"] = df[date_col].dt.isocalendar().week
    df["month"] = df[date_col].dt.month
    df["year"] = df[date_col].dt.year

    df = df.sort_values(by=["Store", date_col], ascending=True)
    df.set_index(date_col, inplace=True, drop=False)
    df.rename(columns={"Date": "date"}, inplace=True)
    return df
