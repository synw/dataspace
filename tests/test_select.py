import polars as pl
from polars.testing import assert_frame_equal
import dataspace

from tests.base import BaseDsTest

ds = dataspace.from_df(pl.DataFrame())


class TestDsDataSelect(BaseDsTest):
    def test_unique(self):
        df1 = pl.DataFrame(
            {"col1": ["one", "one", "three"], "col2": ["two", "two", "four"]}
        )
        ds.df = df1
        data = ds.unique_("col1")
        res = ["one", "three"]
        self.assertEqual(data, res)

    def test_wunique(self):
        df1 = pl.DataFrame({"col": ["one", "one", "two", "two", "two", "three"]})
        ds.df = df1
        df = ds.wunique_("col").sort("col")
        df2 = pl.DataFrame(
            {"col": ["two", "one", "three"], "Number": [3, 2, 1]},
        )
        df2 = df2.with_columns([pl.col("Number").cast(pl.UInt32)])
        df2 = df2.sort("col")
        assert_frame_equal(df, df2)

    def test_limit(self):
        df1 = pl.DataFrame(
            {"col1": ["one", "one", "three"], "col2": ["two", "two", "four"]}
        )
        ds.df = df1
        ds.limit(1)
        df2 = pl.DataFrame({"col1": ["one"], "col2": ["two"]})
        assert_frame_equal(ds.df, df2)
