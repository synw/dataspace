from typing import Optional
import numpy as np
import pandas as pd


def _to_date(df: pd.DataFrame, *cols: str, **kwargs):
    try:
        for col in cols:
            df[col] = pd.to_datetime(df[col], **kwargs)
    except Exception as e:
        raise Exception("Can not convert to date", e)


def _fdate(df: pd.DataFrame, *cols, precision: str = "S", format: Optional[str]):
    def formatdate(row):
        return row.strftime(format)

    def convert(row):
        encoded = "%Y-%m-%d %H:%M:%S"
        if precision == "Min":
            encoded = "%Y-%m-%d %H:%M"
        elif precision == "H":
            encoded = "%Y-%m-%d %H"
        elif precision == "D":
            encoded = "%Y-%m-%d"
        elif precision == "M":
            encoded = "%Y-%m"
        elif precision == "Y":
            encoded = "%Y"
        return row.strftime(encoded)

    for f in cols:
        if format is None:
            df[f] = pd.to_datetime(df[f]).apply(convert)
        else:
            df[f] = pd.to_datetime(df[f]).apply(formatdate)


def _timestamps(df: pd.DataFrame, col: str, name: Optional[str] = None, **kwargs):
    if "errors" not in kwargs:
        kwargs["errors"] = "coerce"
    if "unit" in kwargs:
        kwargs["unit"] = "ms"
    _name = name or "timestamp"
    df[_name] = pd.to_datetime(df[col], **kwargs)
    df[_name] = df[_name].values.astype(np.int64) // 10**9
