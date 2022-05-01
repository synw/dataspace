from typing import List
import pandas as pd


def _append(df: pd.DataFrame, *vals: List, ignore_index=True) -> pd.DataFrame:
    try:
        return pd.concat(
            [df, pd.DataFrame([vals], columns=df.columns)], ignore_index=ignore_index
        )
    except Exception as e:
        raise Exception("Can not append row", e)


def _apply(
    df: pd.DataFrame, function, *cols: List[str], axis=1, **kwargs
) -> pd.DataFrame:
    try:
        if len(cols) == 0:
            df = df.apply(function, axis=axis, **kwargs)
        else:
            _cols = list(cols)
            df[_cols] = df[_cols].apply(function, **kwargs)
    except Exception as e:
        raise Exception("Can not apply function", e)
    return df
