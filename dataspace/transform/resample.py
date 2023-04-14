from typing import Optional, List
from dataspace.utils.messages import msg_ok
import polars as pl


def _resample(
    df: pl.DataFrame,
    date_col: str,
    time_period: str,
    mean_cols: List[str],
    sum_cols: List[str],
) -> pl.DataFrame:
    agg_cols = []
    for col in mean_cols:
        agg_cols.append(pl.col(col).mean())
    for col in sum_cols:
        agg_cols.append(pl.col(col).sum())
    agg_cols.append(pl.count())

    ndf = df.groupby_dynamic(date_col, every=time_period).agg(agg_cols)
    msg_ok("Data resampled by", time_period)
    return ndf
