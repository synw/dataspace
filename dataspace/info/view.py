from typing import Union
import pandas as pd
from dataspace.utils.messages import msg_info
from dataspace.utils.colors import colors
from dataspace.core.env import is_running_in_browser


def _show(rows: int, df: pd.DataFrame) -> Union[pd.DataFrame, str]:
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
    # check if running a Pyodide kernel in the browser
    if is_running_in_browser is True:
        html = (
            f'<p class="msg">The dataframe has <b>{num_rows}</b> rows and <b>{num}</b> '
            f"columns {fields}</p>\n"
        )
        return html + df.head(rows).to_html()
    msg_info(
        "The dataframe has",
        colors.bold(num_rows),
        "rows and",
        colors.bold(num),
        "columns:",
        fields,
    )
    return df.head(rows)
