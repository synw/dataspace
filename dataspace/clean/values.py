import pandas as pd


def _strip(df: pd.DataFrame, *cols: str):
    def remove_ws(row):
        row = str(row).strip()
        return row

    for col in cols:
        df[col] = df[col].apply(remove_ws)


def _strip_cols(df: pd.DataFrame):
    cols = {}
    skipped = []
    for col in df.columns.values:
        try:
            cols[col] = col.strip()
        except Exception:
            skipped.append(str(col))
    df.rename(columns=cols, inplace=True)
    if len(skipped) > 0:
        print("Skipped columns", ",".join(skipped), "while removing white spaces")


def _roundvals(df: pd.DataFrame, col: str, precision: int):
    df[col] = df[col].astype("float64")
    df[col] = df[col].apply(lambda x: round(x, precision))


def _replace(df: pd.DataFrame, col: str, searchval: str, replaceval: str):
    df[col] = df[col].replace(searchval, replaceval)
