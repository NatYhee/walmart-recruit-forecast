from typing import Dict
import pandas as pd


class Naive_Seasonal_Year_1lag:
    def __init__(self, data: pd.DataFrame, ts_col: str) -> None:
        self.data = data
        self.ts_col = ts_col

    def pred(self, pred_col: str = "pred_naive_lag1y") -> pd.DataFrame:
        pred_data = self.data.sort_values(by=["week", "Store", "year"], ascending=True).copy(deep=True)
        pred_data[pred_col] = pred_data.groupby(["week", "Store"]).sales.shift(1)
        pred_data = pred_data[["Store", pred_col]]
        return pred_data
