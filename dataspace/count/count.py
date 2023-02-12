import pandas as pd
from numpy import where

from dataspace.utils.messages import msg_ok, msg_warning


def _count_null_(df: pd.DataFrame, col: str) -> int:
    n = 0
    try:
        n = df[col].isnull().sum()
        msg_ok("Found", n, "nulls in column", col)
    except KeyError as e:
        msg_warning("Can not find column", col)
        raise e
    return n


def _count_empty_(df: pd.DataFrame, col: str) -> int:
    df2 = df[[col]]
    vals = where(df2.applymap(lambda x: x == ""))
    n = len(vals[0])
    msg_ok("Found", n, "empty rows in column " + col)
    return n


def _count_zero_(df: pd.DataFrame, col: str) -> int:
    n: int
    df2 = df[[col]]
    vals = where(df2.applymap(lambda x: x == 0))
    n = len(vals[0])
    msg_ok("Found", n, "zero values in column", col)
    return n


def _count_unique_(df: pd.DataFrame, col: str) -> int:
    n: int
    n = df[col].nunique()
    msg_ok("Found", n, "unique values in column", col)
    return n
