import pandas as pd
import numpy as np


def _to_int(df: pd.DataFrame, *cols, **kwargs):
    for col in cols:
        df[col] = pd.to_numeric(df[col], **kwargs)


def _to_float(df: pd.DataFrame, *cols: str, **kwargs):
    for col in cols:
        df[col] = df[col].astype(np.float64, **kwargs)


def _to_type(df: pd.DataFrame, dtype: type, *cols, **kwargs):
    allcols = df.columns.values
    for col in cols:
        if col not in allcols:
            raise ValueError("Column " + col + " not found")
        df[col] = df[col].astype(dtype, **kwargs)
