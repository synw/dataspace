from typing import Iterable

from numpy import nan
import pandas as pd

from dataspace.utils.messages import msg_ok


def _diffn(
    df: pd.DataFrame,
    diffcol: str,
    name: str = "Diff",
    doround=True,
    percent: bool = False,
) -> pd.DataFrame:
    try:
        vals = []
        i = 0
        for _, row in df.iterrows():
            current = row[diffcol]
            try:
                nextv = df[diffcol].iloc[i + 1]
            except Exception:
                vals.append(nan)
                continue
            val: float
            if percent is False:
                val = current - nextv
            else:
                val = ((current - nextv) * 100) / nextv
            if doround is True:
                val = round(val, 2)
            vals.append(val)
            i += 1
        df[name] = vals
    except Exception as e:
        raise Exception("Can not diff column", e)
    msg_ok("Diff column " + name + " added to the dataframe")
    return df


def _diffp(
    df: pd.DataFrame,
    diffcol: str,
    name: str = "Diff",
    doround=True,
    percent: bool = False,
) -> pd.DataFrame:
    try:
        previous = 0
        i = 0
        vals = [df[diffcol].iloc[0]]
        for _, row in df.iterrows():
            if i == 0:
                vals = [0]
            else:
                val: float
                if percent is False:
                    val = row[diffcol] - previous
                else:
                    val = ((row[diffcol] - previous) * 100) / previous
                if doround is True:
                    val = round(val, 2)
                vals.append(val)
            previous = row[diffcol]
            i = 1
        df[name] = vals
    except Exception as e:
        raise Exception("Can not diff column", e)
    msg_ok("Diff column " + name + " added to the dataframe")
    return df


def _diffm(
    df: pd.DataFrame,
    diffcol: str,
    name: str = "Diff",
    default=nan,
    doround: bool = True,
    percent: bool = False,
) -> pd.DataFrame:
    try:
        mean = df[diffcol].mean()
        vals = []
        for _, row in df.iterrows():
            num = row[diffcol]
            if num > 0:
                diff: str
                if percent is True:
                    diff = num - mean
                else:
                    diff = ((num - mean) * 100) / mean
                if doround is True:
                    diff = round(diff, 2)
                vals.append(diff)
            else:
                vals.append(default)
        df[name] = vals
    except Exception as e:
        raise Exception("Can not diff column", e)
    msg_ok("Diff column " + name + " added to the dataframe")
    return df


def _diffs(
    df: pd.DataFrame, col: str, serie: Iterable, name: str = "Diff"
) -> pd.DataFrame:
    try:
        d = []
        for i, row in df.iterrows():
            v = row[col] - serie[i]
            d.append(v)
        df[name] = d
    except Exception as e:
        raise Exception("Can not diff column from serie", e)
    msg_ok("Diff column " + name + " added to the dataframe")
    return df


def _diffsp(
    df: pd.DataFrame, col: str, serie: Iterable, name: str = "Diff"
) -> pd.DataFrame:
    try:
        d = []
        for i, row in df.iterrows():
            v = (row[col] * 100) / serie[i]
            d.append(v)
        df[name] = d
    except Exception as e:
        raise Exception("Can not diff column from serie", e)
    msg_ok("Diff column " + name + " added to the dataframe")
    return df
