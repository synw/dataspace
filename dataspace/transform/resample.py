from typing import Optional
from dataspace.utils.messages import msg_ok
import pandas as pd


def _resample_(
    df: pd.DataFrame,
    method: str,
    time_period: str,
    num_col: str,
    dateindex: Optional[str] = None,
) -> pd.DataFrame:
    try:
        if dateindex is not None:
            try:
                index = pd.DatetimeIndex(df[dateindex])
                df.set_index(index, inplace=True)
            except Exception as e:
                raise Exception("Can not process date index", e)
        df[num_col] = 1
        df = df.resample(time_period)
        if method == "sum":
            df = df.sum()
        elif method == "mean":
            num_vals = df[num_col].sum()
            df = df.mean()
            df[num_col] = num_vals
        else:
            raise Exception("Resampling method " + method + " unknown")
        msg_ok("Data resampled by", time_period)
        return df
    except Exception as e:
        raise Exception("Can not resample data", e)


def _rsum(
    df: pd.DataFrame,
    time_period: str,
    num_col: str = "Number",
    dateindex: Optional[str] = None,
) -> pd.DataFrame:
    try:
        return _resample_(df, "sum", time_period, num_col, dateindex)
    except Exception as e:
        raise Exception("Can not sum data", e)


def _rmean(
    df: pd.DataFrame,
    time_period: str,
    num_col: str = "Number",
    dateindex: Optional[str] = None,
):
    try:
        return _resample_(df, "mean", time_period, num_col, dateindex)
    except Exception as e:
        raise Exception("Can not mean data", e)
