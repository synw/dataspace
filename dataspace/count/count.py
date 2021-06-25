import pandas as pd
from numpy import where

from dataspace.utils.messages import msg_ok, msg_warning


def _count_null_(df: pd.DataFrame, col: str) -> int:
    n: int
    try:
        n = df[col].isnull().sum()
    except KeyError:
        msg_warning("Can not find column", col)
        return
    except Exception as e:
        msg_warning(e, "Can not count nulls")
    msg_ok("Found", n, "nulls in column", col)
    return n


def _count_empty_(df: pd.DataFrame, col: str) -> int:
    n: int
    try:
        df2 = df[[col]]
        vals = where(df2.applymap(lambda x: x == ""))
        n = len(vals[0])
    except Exception as e:
        msg_warning(e, "Can not count empty values")
        return
    msg_ok("Found", n, "empty strings in column " + col)
    return n


def _count_zero_(df: pd.DataFrame, col: str) -> int:
    n: int
    try:
        df2 = df[[col]]
        vals = where(df2.applymap(lambda x: x == 0))
        n = len(vals[0])
    except Exception as e:
        msg_warning(e, "Can not count zero values")
        return
    msg_ok("Found", n, "zero values in column", col)
    return n


def _count_unique_(df: pd.DataFrame, col: str) -> int:
    n: int
    try:
        n = df[col].nunique()
    except Exception as e:
        msg_warning(e, "Can not count unique values")
        return
    msg_ok("Found", n, "unique values in column", col)
    return n
