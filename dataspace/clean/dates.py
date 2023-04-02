import polars as pl


def _to_tzdate(df: pl.DataFrame, *cols: str) -> pl.DataFrame:
    new_cols = [
        pl.col(col).str.strptime(
            pl.Datetime, fmt="%Y-%m-%d %H:%M:%S.%f%z", strict=False
        )
        for col in cols
    ]
    return df.with_columns(new_cols)


def _to_date(
    df: pl.DataFrame, *cols: str, fmt: str = "%Y-%m-%d %H:%M:%S"
) -> pl.DataFrame:
    new_cols = [
        pl.col(col).str.strptime(pl.Datetime, fmt=fmt, strict=False) for col in cols
    ]
    return df.with_columns(new_cols)


def _fdate(
    df: pl.DataFrame, *cols: str, precision: str = "S", newcol: str
) -> pl.DataFrame:
    for col in cols:
        if df[col].dtype != pl.Datetime:
            raise ValueError("Formated dates can only be produced from a date column")
    encoded: str | None = None
    if precision == "S":
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
    if encoded:
        return df.with_columns(
            [pl.col(col).dt.strftime(encoded).alias(newcol) for col in cols]
        )
    else:
        raise ValueError(f"Unknon precision {precision}")


def _timestamps(df: pl.DataFrame, *cols: str, name: str) -> pl.DataFrame:
    for col in cols:
        if df[col].dtype != pl.Datetime:
            raise ValueError("Timestamps can only be produced from a date column")
    return df.with_columns([pl.col(col).dt.timestamp().alias(name) for col in cols])
