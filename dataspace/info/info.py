import pandas as pd


def _cols(df: pd.DataFrame) -> pd.DataFrame:
    s = df.iloc[0]
    df = pd.DataFrame(s)
    df = df.rename(columns={0: "value"})

    def run(row):
        t = row[0]
        return type(t).__name__

    s = df.apply(run, axis=1)
    df = df.rename(columns={0: "value"})
    df["types"] = s
    return df
