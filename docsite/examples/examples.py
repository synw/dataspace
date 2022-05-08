import numpy as np
import pandas as pd
import dataspace


def add():
    df = pd.DataFrame(np.linspace(1, 100, 5), columns=["num"])
    ds = dataspace.from_df(df)
    print("Adding a column with default value")
    ds.add("num2", 1)
    ds.show()
