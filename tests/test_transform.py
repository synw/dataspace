import polars as pl
from polars.testing import assert_frame_equal
import dataspace

from tests.base import BaseDsTest

ds = dataspace.from_df(pl.DataFrame())


class TestDsDataTransform(BaseDsTest):
    def test_keep(self):
        df1 = pl.DataFrame({"one": [1, 1], "two": [2, 2]})
        ds.df = df1
        ds.keep("one")
        df2 = pl.DataFrame({"one": [1, 1]})
        assert_frame_equal(ds.df, df2)

    def test_rsum(self):
        df1 = pl.DataFrame(
            {
                "date": ["2001/01/01", "2001/02/01", "2001/02/15", "2001/02/28"],
                "value": [1, 5, 3, 3],
            }
        )
        ds.df = df1
        ds.to_date("date", fmt="%Y/%m/%d")
        ds.rsum("date", time_period="1mo")
        df2 = pl.DataFrame(
            {
                "date": [
                    "2001-01-01 00:00:00.000000",
                    "2001-02-01 00:00:00.000000",
                ],
                "count": [1, 3],
            }
        )
        ds.to_str("date")
        df2 = df2.with_columns([pl.col("count").cast(pl.UInt32)])
        assert_frame_equal(ds.df, df2)

    def test_rmean(self):
        df1 = pl.DataFrame(
            {
                "date": ["2001/01/01", "2001/01/02", "2001/02/15", "2001/02/28"],
                "value": [1, 2, 1, 2],
            }
        )
        ds.df = df1
        ds.to_date("date", fmt="%Y/%m/%d")
        ds.rmean("date", time_period="1mo")
        df2 = pl.DataFrame(
            {
                "date": [
                    "2001-01-01 00:00:00.000000",
                    "2001-02-01 00:00:00.000000",
                ],
                "count": [2, 2],
            }
        )
        ds.to_str("date")
        df2 = df2.with_columns([pl.col("count").cast(pl.UInt32)])
        assert_frame_equal(ds.df, df2)

    def test_sort(self):
        df1 = pl.DataFrame({"col": [2, 1]})
        ds.df = df1
        df2 = pl.DataFrame({"col": [1, 2]})
        ds.sort("col")
        assert_frame_equal(ds.df, df2)

    def test_replace(self):
        df1 = pl.DataFrame({"one": [1, 1], "two": [2, 2]})
        ds.df = df1
        df2 = pl.DataFrame({"one": [2, 2], "two": [2, 2]})
        ds.replace("one", 1, 2)
        assert_frame_equal(ds.df, df2)

    def test_split(self):
        df1 = pl.DataFrame({"val": [1, 2, 1, 2]})
        ds.df = df1
        dsd = ds.split_("val")
        d = "{1: <DataSpace object | 2 rows>, 2: <DataSpace object | 2 rows>}"
        self.assertEqual(str(dsd), d)

    def test_drop(self):
        df1 = pl.DataFrame({"one": [1, 1], "two": [2, 2]})
        ds.df = df1
        ds.drop("two")
        df2 = pl.DataFrame({"one": [1, 1]})
        assert_frame_equal(ds.df, df2)

    def test_exclude(self):
        df1 = pl.DataFrame({"one": [2, 1], "two": [2, 2]})
        ds.df = df1
        ds.exclude("one", 1)
        df2 = pl.DataFrame({"one": [2], "two": [2]})
        assert_frame_equal(ds.df, df2)
