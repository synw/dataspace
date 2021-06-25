from typing import List
import pandas as pd


def _append(df: pd.DataFrame, vals: list, index=None) -> pd.DataFrame:
    try:
        if index is not None:
            return df.append(
                pd.DataFrame(columns=df.columns, data=[vals], index=[index])
            )
        else:
            return df.append(
                pd.DataFrame(
                    data=[vals],
                    columns=df.columns,
                )
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
            cols = list(cols)
            df[cols] = df[cols].apply(function, **kwargs)
    except Exception as e:
        raise Exception("Can not apply function", e)
    return df
