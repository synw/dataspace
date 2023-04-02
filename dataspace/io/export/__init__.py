import polars as pl
from dataspace.utils.messages import msg_start, msg_end


def export_csv(df: pl.DataFrame, filepath: str, **kwargs):
    msg_start("Saving data to " + filepath + " ...")
    df.write_csv(filepath, **kwargs)
    msg_end("Data exported to", filepath)
