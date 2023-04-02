from typing import Any
import polars as pl


def _strip(df: pl.DataFrame, *cols: str) -> pl.DataFrame:
    def remove_ws(row):
        row = str(row).strip()
        return row

    for col in cols:
        df = df.with_columns([df[col].apply(remove_ws).alias(col)])
    return df


def _strip_cols(df: pl.DataFrame) -> pl.DataFrame:
    cols = {}
    skipped = []
    for col in df.columns:
        try:
            cols[col] = col.strip()
        except Exception:
            skipped.append(str(col))

    df = df.select([df[col].alias(new_col) for col, new_col in cols.items()])

    if len(skipped) > 0:
        print("Skipped columns", ",".join(skipped), "while removing white spaces")
    return df


def _roundvals(df: pl.DataFrame, col: str, precision: int) -> pl.DataFrame:
    new_col = (
        df[col]
        .cast(pl.Float64)
        .apply(lambda x: round(x, precision), return_dtype=pl.Float64)
        .alias(col)
    )
    df = df.with_columns([new_col])
    return df


def _replace(
    df: pl.DataFrame, col: str, searchval: Any, replaceval: Any
) -> pl.DataFrame:
    new_col = (
        df[col]
        .apply(
            lambda x: replaceval if x == searchval else x, return_dtype=df[col].dtype
        )
        .alias(col)
    )
    df = df.with_columns([new_col])
    return df
