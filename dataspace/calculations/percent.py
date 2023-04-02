import polars as pl


def _percent(df: pl.DataFrame, col: str, roundn: int) -> pl.DataFrame:
    _sum = df.select(pl.sum(col))[0, 0]
    return df.with_columns(
        [pl.col(col).apply(lambda x: round((x / _sum) * 100, roundn)).alias("percent")]
    )
