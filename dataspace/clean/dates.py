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

    try:
        for f in cols:
            try:
                if format is None:
                    df[f] = pd.to_datetime(df[f]).apply(convert)
                else:
                    df[f] = pd.to_datetime(df[f]).apply(formatdate)
            except ValueError as e:
                raise Exception("Can not convert date", e)
    except KeyError:
        raise Exception("Can not find colums " + " ".join(cols))
    except Exception as e:
        raise Exception(e, "Can not process date col")


def _timestamps(df: pd.DataFrame, col: str, **kwargs):
    try:
        name = "timestamp"
        if "name" in kwargs:
            name = kwargs["name"]
        if "errors" not in kwargs:
            kwargs["errors"] = "coerce"
        if "unit" in kwargs:
            kwargs["unit"] = "ms"
        df[name] = pd.to_datetime(df[col], **kwargs)
        df[name] = df["timestamp"].values.astype(np.int64) // 10 ** 9
    except Exception as e:
        raise Exception("Can not convert to timestamps", e)
