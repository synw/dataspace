import polars as pl

from dataspace.utils.messages import msg_info
from dataspace.utils.colors import colors
from dataspace.core.env import is_running_in_browser


def _show(rows: int, df: pl.DataFrame) -> pl.DataFrame:
    
    num_cols = 0
    num_rows = 0
    try:
        num_rows = df.select(pl.count())[0,0]
        num_cols = len(df.columns)
    except Exception as e:
        raise ValueError("Can not show dataframe", e)
    fds = []
    for fi in df.columns:
        fds.append(str(fi))
    fields = ", ".join(fds)
    # check if running a Pyodide kernel in the browser
    """if is_running_in_browser is True:
        html = (
            f'<p class="msg">The dataframe has <b>{num_rows}</b> rows and <b>{num_cols}</b> '
            f"columns {fields}</p>\n"
        )
        return html + df.head(rows).to_html()"""
    msg_info(
        "The dataframe has",
        colors.bold(num_rows),
        "rows and",
        colors.bold(num_cols),
        "columns:",
        fields,
    )
    return df.head(rows)
