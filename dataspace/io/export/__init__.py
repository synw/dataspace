import pandas as pd
from dataspace.utils.messages import msg_start, msg_end


def _export_csv(df: pd.DataFrame, filepath: str, **kwargs) -> None:
    try:
        msg_start("Saving data to " + filepath + " ...")
        df.to_csv(filepath, encoding="utf-8", **kwargs)
        msg_end("Data exported to", filepath)
    except Exception as e:
        raise Exception("Can not convert data to csv", e)
