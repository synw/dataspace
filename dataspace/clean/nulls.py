from typing import Any, List, Literal, Sequence
import polars as pl


def _drop_any_nulls(df: pl.DataFrame, *cols: str) -> pl.DataFrame:
    return df.drop_nulls(subset=cols)


def _drop_all_nulls(df: pl.DataFrame) -> pl.DataFrame:
    return df.filter(~pl.all(pl.all().is_null()))


def _fill_nulls(
    df: pl.DataFrame, *cols: str, nulls: List[Any], val: Any
) -> pl.DataFrame:
    if len(cols) == 0:
        cols = tuple(df.columns)
    return df.with_columns(
        [
            pl.when(pl.col(col).is_in(nulls))
            .then(pl.lit(val))
            .otherwise(pl.col(col))
            .alias(col)
            for col in cols
        ]
    )


def _dropna(
    df: pl.DataFrame,
    *subset: str,
    how: Literal["any", "all"] = "any",
) -> pl.DataFrame:
    """
    Remove null and NaN values
    """
    if len(subset) == 0:
        subset = pl.all()
    else:
        subset = pl.col(subset)
    if how == "any":
        result = df.filter(pl.all(subset.is_not_null() & subset.is_not_nan()))
    elif how == "all":
        result = df.filter(pl.any(subset.is_not_null() & subset.is_not_nan()))
    return result
