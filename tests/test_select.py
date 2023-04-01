import pandas as pd
from polars.testing import assert_frame_equal
import dataspace

from tests.base import BaseDsTest

ds = dataspace.from_df(pd.DataFrame())


class TestDsDataSelect(BaseDsTest):
    def test_unique(self):
        df1 = pd.DataFrame(
            {"col1": ["one", "one", "three"], "col2": ["two", "two", "four"]}
        )
        ds.df = df1
        data = ds.unique_("col1")
        res = ["one", "three"]
        self.assertEqual(data, res)

    def test_wunique(self):
        df1 = pd.DataFrame({"col": ["one", "one", "two", "two", "two", "three"]})
        ds.df = df1
        df = ds.wunique_("col")
        df2 = pd.DataFrame({"Number": [3, 2, 1]}, ["two", "one", "three"])
        assert_frame_equal(df, df2)

    def test_limit(self):
        df1 = pd.DataFrame([["one", "three"], ["two", "four"]])
        ds.df = df1
        ds.limit(1)
        df2 = pd.DataFrame([["one", "three"]])
        assert_frame_equal(ds.df, df2)
