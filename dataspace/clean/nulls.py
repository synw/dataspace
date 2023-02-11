from typing import List, Literal, Optional, Union
import pandas as pd


def _drop_nan(
    df: pd.DataFrame,
    col: Optional[Union[str, List[str]]] = None,
    how: Literal["all", "any"] = "all",
    **kwargs
) -> pd.DataFrame:
    try:
        if col is None:
            df = df.dropna(how=how, **kwargs)
        else:
            df = df.dropna(subset=col, how=how, **kwargs)
        # df.reset_index(drop=True)
        return df
    except Exception as e:
        raise Exception("Error dropping nan values", e)


def _fill_nan(df: pd.DataFrame, val, *cols: str) -> pd.DataFrame:
    if len(cols) == 0:
        cols = df.columns.values
    for col in cols:
        df[col].fillna(val, inplace=True)
    return df


def _fill_nulls(df: pd.DataFrame, val, *cols: str, nulls) -> pd.DataFrame:
    if len(cols) == 0:
        cols = df.columns.values
    for col in cols:
        df[col].replace(nulls, val, inplace=True)
    return df
