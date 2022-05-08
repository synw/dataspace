import numpy as np
import pandas as pd
import dataspace


def add():
    df = pd.DataFrame(np.linspace(1, 100, 1000))
    ds = dataspace.from_df(df)
    print(ds.df.to_html())
