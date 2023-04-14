from typing import Any
import polars as pl
from ..utils.messages import msg_info


def _drop(df: pl.DataFrame, *cols: str) -> pl.DataFrame:
    ndf = df.drop(cols)
    msg_info("Columns", *cols, "droped")
    return ndf


def _rename(df: pl.DataFrame, source_col: str, dest_col: str) -> pl.DataFrame:
    ndf = df.rename({source_col: dest_col})
    msg_info("Column", source_col, "renamed")
    return ndf


def _add(df: pl.DataFrame, col: str, value: Any) -> pl.DataFrame:
    ndf = df.with_columns([pl.lit(value).alias(col)])
    msg_info("Column", col, "added")
    return ndf


def _indexcol(df: pl.DataFrame, col: str) -> pl.DataFrame:
    return df.with_columns([pl.Series(list(range(df.height))).alias(col)])
