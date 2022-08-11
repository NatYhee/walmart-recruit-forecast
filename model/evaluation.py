import pandas as pd

from copy import deepcopy


def wmae_holiday_weight(
    data: pd.DataFrame,
    prediction_cols: list,
    target_col: str = "sales",
    eval_period: str = "train",
) -> pd.DataFrame:
    evaluation_df = deepcopy(data)
    evaluation_df["weight_wmae"] = evaluation_df["IsHoliday"].apply(
        lambda holiday: 5 if holiday else 1
    )

    evaluation_df["percent_weight_wmae"] = evaluation_df["weight_wmae"]/evaluation_df["weight_wmae"].sum()

    prediction_eval_cols = []
    prediction_eval_results = []

    for prediction in prediction_cols:
        eval_col_name = f"wmae_point_{prediction}"
        prediction_eval_cols.append(eval_col_name)

        evaluation_df[eval_col_name] = (
            evaluation_df["percent_weight_wmae"] * (evaluation_df[prediction] - evaluation_df[target_col]).abs()
        )
        print(evaluation_df[["Store", "sales", "pred_naive_lag1y", eval_col_name, "percent_weight_wmae"]])
        eval_result = evaluation_df[eval_col_name].sum()
        prediction_eval_results.append(eval_result)

    wmae_holiday_weight_result = pd.DataFrame(
        {
            "prediction": prediction_cols,
            f"wmae_holiday_{eval_period}": prediction_eval_results,
        }
    )

    return wmae_holiday_weight_result
