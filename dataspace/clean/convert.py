import polars as pl


def _to_int(df: pl.DataFrame, *cols) -> pl.DataFrame:
    new_cols = [pl.col(col).cast(pl.Int64) for col in cols]
    return df.with_columns(new_cols)


def _to_float(df: pl.DataFrame, *cols: str) -> pl.DataFrame:
    new_cols = [pl.col(col).cast(pl.Float64) for col in cols]
    return df.with_columns(new_cols)


def _to_str(df: pl.DataFrame, *cols: str) -> pl.DataFrame:
    new_cols = [pl.col(col).cast(pl.Utf8) for col in cols]
    return df.with_columns(new_cols)


def _to_type(df: pl.DataFrame, dtype: pl.DataType, *cols) -> pl.DataFrame:
    new_cols = [pl.col(col).cast(dtype) for col in cols]
    return df.with_columns(new_cols)
