import polars as pl


def _to_tzdate(df: pl.DataFrame, *cols: str) -> pl.DataFrame:
    new_cols = [
        pl.col(col).str.strptime(
            pl.Datetime, fmt="%Y-%m-%d %H:%M:%S.%f%z", strict=False
        )
        for col in cols
    ]
    return df.with_columns(new_cols)


def _to_date(df: pl.DataFrame, *cols: str) -> pl.DataFrame:
    new_cols = [pl.col(col).str.strptime(pl.Datetime, strict=False) for col in cols]
    return df.with_columns(new_cols)


def _fdate(df: pl.DataFrame, *cols: str, newcol: str, precision: str) -> pl.DataFrame:
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

    print("Enc", encoded)
    return df.with_columns(
        [pl.col(col).dt.strftime(encoded).alias("fdate") for col in cols]
    )


def _timestamps(df: pl.DataFrame, *cols: str, name: str) -> pl.DataFrame:
    return df.with_columns([pl.col(col).dt.timestamp().alias(name) for col in cols])
