import polars as pl


def _cvar(df: pl.DataFrame, col: str) -> float:
    """
    Returns the coefficient of variance of a column
    in percentage
    """
    return df.select([(pl.col("col").std() / pl.col("col").mean()) * 100])[0, 0]
