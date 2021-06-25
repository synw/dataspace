import pandas as pd
from ..utils.messages import msg_warning, msg_info


def _drop(df: pd.DataFrame, *cols) -> pd.DataFrame:
    try:
        index = df.columns.values
        for col in cols:
            if col not in index:
                msg_warning("Column", col, "not found. Aborting")
                return
            df = df.drop(col, axis=1)
    except Exception as e:
        raise ("Can not drop column", e)
    return df


def _rename(df: pd.DataFrame, source_col: str, dest_col: str) -> pd.DataFrame:
    try:
        df = df.rename(columns={source_col: dest_col})
    except Exception as e:
        raise ("Can not rename column", e)
    msg_info("Column", source_col, "renamed")
    return df
