import pandas as pd
import numpy as np


def _to_int(df: pd.DataFrame, *cols, **kwargs):
    try:
        for col in cols:
            df[col] = pd.to_numeric(df[col], **kwargs)
    except Exception as e:
        raise Exception("Can not convert column values to integer", e)


def _to_float(df: pd.DataFrame, *cols: str, **kwargs):
    try:
        for col in cols:
            df[col] = df[col].astype(np.float64, **kwargs)
    except Exception as e:
        raise Exception("Error converting to float", e)


def _to_type(df: pd.DataFrame, dtype: type, *cols, **kwargs):
    try:
        allcols = df.columns.values
        for col in cols:
            if col not in allcols:
                raise Exception("Column " + col + " not found")
            df[col] = df[col].astype(dtype, **kwargs)
    except Exception as e:
        raise Exception("Can not convert to type", e)
