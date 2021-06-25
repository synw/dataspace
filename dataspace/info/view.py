import pandas as pd
from dataspace.utils.messages import msg_info
from dataspace.utils.colors import colors


def _show(rows: int, df: pd.DataFrame) -> pd.DataFrame:
    num = 0
    try:
        num = len(df.columns.values)
    except Exception as e:
        raise ValueError("Can not show dataframe", e)
        return
    f = list(df)
    fds = []
    for fi in f:
        fds.append(str(fi))
    fields = ", ".join(fds)
    num_rows = len(df.index)
    msg_info(
        "The dataframe has",
        colors.bold(num_rows),
        "rows and",
        colors.bold(num),
        "columns:",
        fields,
    )
    return df.head(rows)
