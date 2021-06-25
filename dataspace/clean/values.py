import pandas as pd


def _strip(df: pd.DataFrame, *cols: str):
    def remove_ws(row):
        row = str(row).strip()
        return row

    try:
        for col in cols:
            df[col] = df[col].apply(remove_ws)
    except Exception as e:
        raise Exception("Can not remove white space in column", e)


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
    try:
        df[col] = df[col].astype("float64")
        df[col] = df[col].apply(lambda x: round(x, precision))
    except Exception as e:
        raise Exception("Can not round column values", e)


def _replace(df: pd.DataFrame, col: str, searchval: str, replaceval: str):
    try:
        df[col] = df[col].replace(searchval, replaceval)
    except Exception as e:
        raise Exception("Can not replace value in column", e)
