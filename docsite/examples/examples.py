import numpy as np
import pandas as pd
import dataspace


def add():
    df = pd.DataFrame(np.linspace(1, 100, 5), columns=["num"])
    ds = dataspace.from_df(df)
    print("Adding a column with default value")
    ds.add("num2", 1)
    ds.show()


def bar_():
    data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.bar_("col1:N", "col2:Q").to_json()  # type: ignore
