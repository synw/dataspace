import polars as pl

from dataspace.utils.messages import msg_ok, msg_warning


def _count_null_(df: pl.DataFrame, col: str) -> int:
    n = 0
    try:
        count_df = df.select(pl.col(col).is_null().sum())
        n = count_df[0, 0]
        msg_ok("Found", n, "nulls in column", col)
    except KeyError as e:
        msg_warning("Can not find column", col)
        raise e
    return n


def _count_empty_(df: pl.DataFrame, col: str) -> int:
    def check_empty(value):
        return value == ""

    empty_string_count_df = df.with_columns(
        [pl.col(col).apply(check_empty, return_dtype=pl.Boolean).alias("is_empty")]
    ).select(pl.col("is_empty").sum().alias("empty_string_count"))
    n = empty_string_count_df["empty_string_count"][0]
    msg_ok("Found", n, "empty rows in column " + col)
    return n


def _count_zero_(df: pl.DataFrame, col: str) -> int:
    n = df.select((pl.col(col) == 0).sum())[0, 0]
    msg_ok("Found", n, "rows with 0 value in column " + col)
    return n


def _count_unique_(df: pl.DataFrame, col: str) -> int:
    n = len(df[col].unique())
    msg_ok("Found", n, "unique values in column", col)
    return n
