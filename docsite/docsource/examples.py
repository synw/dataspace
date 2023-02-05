import numpy as np
import pandas as pd
import altair as alt
import dataspace


async def load_dataset(url: str) -> dataspace.DataSpace:
    return dataspace.from_df([1])


async def show():
    ds = await load_dataset("bitcoin")
    ds.show()


async def cols_():
    ds = await load_dataset("bitcoin")
    print(ds.cols_())
    ds.show()


def count_null_():
    data = {"col1": [1, np.nan, 2, None, 3, 3]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    n = ds.count_null_("col1")
    print("The column has", n, "nulls")
    ds.show()


def count_empty_():
    data = {"col1": ["foo", "", "bar", ""]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    n = ds.count_empty_("col1")
    print("The column has", n, "empty values")
    ds.show()


def count_zero_():
    data = {"col1": [0, 1, 2, 0, 3, 3]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    n = ds.count_zero_("col1")
    print("The column has", n, "zero values")
    ds.show()


def count_unique_():
    data = {"col1": [1, 2, 2, 3, 3, 3]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    n = ds.count_unique_("col1")
    print("The column has", n, "unique values")
    ds.show()


def wunique_():
    data = {"col1": ["one", "two", "two", "three", "three", "three"]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    df = ds.wunique_("col1")
    print("Dataframe of unique values weights:")
    print(df)


def limit():
    df = pd.DataFrame(np.linspace(1, 100, 1000))
    ds = dataspace.from_df(df)
    print("Initial length:", len(ds.df.index))
    ds.limit(10)
    print("New length after limiting:", len(ds.df.index))
    ds.show()


def unique_():
    data = {"col1": ["A", "B", "C", "A", "B"]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    uv = ds.unique_("col1")
    print("Colum unique values:", uv)
    ds.show()


def drop_nan():
    data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    print("The col1 has", ds.count_null_("col1"), "nulls")
    ds.drop_nan("col1")
    ds.show()


def fill_nan():
    data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.count_null_("col1")
    ds.fill_nan("val", "col1")
    ds.show()


def fill_nulls():
    data = {"col1": np.array([1, None, ""]), "col2": np.array([None, 0, None])}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.count_empty_("col1")
    ds.count_null_("col1")
    ds.fill_nulls()
    ds.show()


async def fdate():
    ds = await load_dataset("timeserie")
    print(ds.df.head())
    ds.fdate("date", precision="D")
    ds.show()


async def to_date():
    ds = await load_dataset("bitcoin")
    print("1. Initial dataframe:")
    print(ds.df.head(1))
    print("2. Colums:")
    print(ds.cols_())
    ds.to_date("ReceiptTS")
    print("3. New column types:", ds.cols_())
    ds.show()


async def timestamps():
    ds = await load_dataset("timeserie")
    print(ds.df.head())
    ds.timestamps("date")
    ds.show()


def to_int():
    data = {"col1": ["5", "8", "3"], "col2": ["8", "7", "2"]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    print("Column types:", ds.cols_())
    ds.to_int("col1", "col2")
    print("Column types after convert:", ds.cols_())
    ds.show()


def to_float():
    data = {"col1": ["0.25", "0.85", "0.58"]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    print("Column types:", ds.cols_())
    ds.to_float("col1")
    print("Column types after convert:", ds.cols_())
    ds.show()


def to_type():
    data = {"col1": [1, 0, 0]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    print("Column types:", ds.cols_())
    ds.to_type(bool, "col1")
    print("Column types after convert:", ds.cols_())
    ds.show()


def strip():
    data = {"col1": [" one ", "two "]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    print(list(ds.df.col1))
    ds.strip("col1")
    print(list(ds.df.col1))
    ds.show()


def strip_cols():
    data = {"col1 ": [1, 2], " col2 ": [3, 4]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    print(list(ds.df.columns.values))
    ds.strip_cols()
    print(list(ds.df.columns.values))
    ds.show()


def roundvals():
    data = {"col1": [1.25889, 1.25874, 1.42587]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.roundvals("col1")
    ds.show()


def replace():
    data = {"col1": ["a", "b", "novalue"]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.replace("col1", "novalue", "c")
    ds.show()


def index():
    data = {"col1": ["a", "b", "c"], "col2": [12, 7, 5]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.index("col1")
    ds.show()


async def dateindex():
    ds = await load_dataset("timeserie")
    ds.dateindex("date")
    ds.show()


async def split_():
    ds = await load_dataset("bitcoin")
    print("Unique values in the sources column:", ds.unique_("Source"))
    dss = ds.split_("Source")
    print("splitted DataSpace objects:", dss.keys())
    dss["FTX"].show()


def indexcol():
    data = {"col1": ["A", "B", "C", "D"]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.indexcol("id")
    ds.show()


def drop():
    data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.drop("col2")
    ds.show()


def add():
    df = pd.DataFrame(np.linspace(1, 100, 5), columns=["num"])
    ds = dataspace.from_df(df)
    print("Adding a column with default value")
    ds.add("num2", 1)
    ds.show()


def rename():
    data = {"col1": [0, 1, 0]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.rename("col1", "new name")
    ds.show()


def keep():
    data = {"col1": [0, 1, 0], "col2": [0, 0, 1], "col3": [1, 1, 1], "col4": [0, 0, 1]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.keep("col1", "col4")
    ds.show()


def copycol():
    data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.copycol("col2", "new col name")
    ds.show()


def sort():
    data = {"col1": [14, 25, 3, 8, 12]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.sort("col1")
    ds.show()


def exclude():
    data = {"col1": [1, 0, 1, 4, 5, 1]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.exclude("col1", 1)
    ds.show()


def dropr():
    data = {"col1": [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.dropr([0, 4])
    ds.show()


def append():
    data = {"col1": [1, 2], "col2": ["foo", "bar"]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.append(0, "baz")
    ds.show()


def reverse():
    data = {"col1": [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.reverse()
    ds.show()


def apply():
    data = {"col1": [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)

    def f(row):
        # add a new column with a value
        row["newcol"] = row["col1"] + 1
        return row

    ds.apply(f)
    ds.show()


async def rsum():
    ds = await load_dataset("bitcoin")
    ds.keep("mktTS", "qty")
    ds.dateindex("mktTS")
    ds.rsum("1S", "Datapoints per second")
    ds.rename("qty", "Market volume")
    ds.show()


async def rmean():
    ds = await load_dataset("bitcoin")
    ds.rmean("1S", "Datapoints per second", dateindex="mktTS")
    ds.rename("px", "Mean price")
    ds.show()


async def axis():
    ds = await load_dataset("sp500")
    ds.axis("date:T", "price:Q")
    ds.line_()


def bar_():
    data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.bar_("col1:N", "col2:Q")


async def line_():
    ds = await load_dataset("sp500")
    ds.axis("date:T", "price:Q")
    ds.line_()


async def point_():
    ds = await load_dataset("sp500")
    ds.axis("date:T", "price:Q")
    ds.point_()


async def area_():
    ds = await load_dataset("sp500")
    ds.axis("date:T", "price:Q")
    ds.area_()


def hline_():
    data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    chart = ds.bar_("col1:N", "col2:Q")
    hline = ds.hline_(style={"color": "green"})
    chart + hline  # type: ignore


def diffm():
    data = {"col1": [1, 2, 3, 4, 4, 6, 8, 10, 12]}
    df = pd.DataFrame(data)
    ds = dataspace.from_df(df)
    ds.diffm("col1")
    ds.indexcol("id")
    ds.axis("id", "col1")
    c = ds.bar_()
    ds.axis("id", "Diff")
    d = ds.line_().encode(color=alt.value("red"))
    c + d  # type: ignore
