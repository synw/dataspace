from typing import Iterable

from numpy import nan
import polars as pl

from dataspace.utils.messages import msg_ok


def _diffp(
    df: pl.DataFrame,
    diffcol: str,
    name: str,
    decimals=0,
    percent: bool = False,
) -> pl.DataFrame:
    if not percent:
        if decimals > 0:
            return df.with_columns(
                [
                    (pl.col(diffcol) - pl.col(diffcol).shift(1))
                    .round(decimals)
                    .alias(name)
                ]
            )
        else:
            return df.with_columns(
                [(pl.col(diffcol) - pl.col(diffcol).shift(1)).alias(name)]
            )
    else:
        if decimals > 0:
            return df.with_columns(
                [
                    (
                        (pl.col(diffcol) - pl.col(diffcol).shift(1))
                        / pl.col(diffcol).shift(1)
                        * 100
                    )
                    .round(decimals)
                    .alias(name)
                ]
            )
        else:
            return df.with_columns(
                [
                    (
                        (pl.col(diffcol) - pl.col(diffcol).shift(1))
                        / pl.col(diffcol).shift(1)
                        * 100
                    ).alias(name)
                ]
            )


def _diffm(
    df: pl.DataFrame,
    diffcol: str,
    name: str = "Diff",
    decimals=0,
    percent: bool = False,
) -> pl.DataFrame:
    if not percent:
        if decimals > 0:
            return df.with_columns(
                [(pl.col(diffcol) - pl.col(diffcol).mean()).round(decimals).alias(name)]
            )
        else:
            return df.with_columns(
                [(pl.col(diffcol) - pl.col(diffcol).mean()).alias(name)]
            )
    else:
        if decimals > 0:
            return df.with_columns(
                [
                    (
                        (pl.col(diffcol) - pl.col(diffcol).mean())
                        / pl.col(diffcol).mean()
                        * 100
                    )
                    .round(decimals)
                    .alias(name)
                ]
            )
        else:
            return df.with_columns(
                [
                    (
                        (pl.col(diffcol) - pl.col(diffcol).mean())
                        / pl.col(diffcol).mean()
                        * 100
                    ).alias(name)
                ]
            )


"""def _diffs(
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
    return df"""
