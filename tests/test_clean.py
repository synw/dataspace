import pytest
import polars as pl
import dataspace
from polars.testing import assert_frame_equal

from tests.base import BaseDsTest

ds = dataspace.from_df(pl.DataFrame())


class TestDsDataClean(BaseDsTest):
    def test_drop_nulls(self):
        df1 = pl.DataFrame({"one": ["one", None], "two": ["two", None]})
        ds.df = df1
        ds.drop_all_nulls()
        df2 = pl.DataFrame({"one": ["one"], "two": ["two"]})
        assert_frame_equal(ds.df, df2)
        ds.df = pl.DataFrame({"one": ["one", None], "two": ["two", "x"]})
        ds.drop_any_nulls("one")
        assert_frame_equal(ds.df, df2)

    def test_replace(self):
        df1 = pl.DataFrame({"one": ["val1", "val2"], "two": ["two", "two"]})
        ds.df = df1
        ds.replace("one", "val2", "val3")
        df2 = pl.DataFrame({"one": ["val1", "val3"], "two": ["two", "two"]})
        assert_frame_equal(ds.df, df2)

    def test_to_int(self):
        df1 = pl.DataFrame({"one": ["val1", "val2"], "two": [1.0, 2.0]})
        ds.df = df1
        ds.to_int("two")
        self.assertEqual(list(ds.df["two"]), [1, 2])
        with pytest.raises(pl.ComputeError):
            ds.df = pl.DataFrame({"one": ["val1", "val2"], "two": ["wrong", 2.0]})
            ds.to_int("two")

    def test_to_float(self):
        df1 = pl.DataFrame({"one": ["val1", "val2"], "two": [1, 2]})
        ds.df = df1
        ds.to_float("two")
        self.assertEqual(list(ds.df["two"]), [1.0, 2.0])
        with pytest.raises(pl.ComputeError):
            ds.df = pl.DataFrame({"one": ["val1", "val2"], "two": ["wrong", 2]})
            ds.to_float("two")

    def test_to_type(self):
        df1 = pl.DataFrame({"one": ["val1", "val2"], "two": [1, 2]})
        ds.df = df1
        ds.to_type(pl.Utf8, "two")  # type: ignore
        df2 = pl.DataFrame({"one": ["val1", "val2"], "two": ["1", "2"]})
        assert_frame_equal(ds.df, df2)
        with pytest.raises(pl.ComputeError):
            ds.df = pl.DataFrame({"one": ["val1", "val2"], "two": ["wrong", 2.0]})
            ds.to_type(pl.Int64, "two")  # type: ignore
        with pytest.raises(pl.ColumnNotFoundError):
            ds.to_type(pl.Utf8, "wrongcol")  # type: ignore

    def tests_timestamps(self):
        df1 = pl.DataFrame(
            {"one": ["val1", "val2"], "two": ["2002/12/01", "2002/12/02"]}
        )
        ds.df = df1
        ds.to_date("two", fmt="%Y/%m/%d")
        ds.timestamps("two", name="ts")
        ds.drop("two")
        df2 = pl.DataFrame(
            {
                "one": ["val1", "val2"],
                "ts": [1038700800000000, 1038787200000000],
            }
        )
        assert_frame_equal(ds.df, df2)
        ds.df = df1
        ds.to_date("two", fmt="%Y/%m/%d")
        ds.timestamps("two")
        with pytest.raises(ValueError):
            ds.timestamps("one")

    def test_strip(self):
        df = pl.DataFrame({"one": [" 2 ", "1 ", "0 "], "two": [2, 1, 1]})
        ds.df = df
        ds.strip("one")
        df2 = pl.DataFrame({"one": ["2", "1", "0"], "two": [2, 1, 1]})
        assert_frame_equal(ds.df, df2)

    def test_strip_cols(self):
        df1 = pl.DataFrame({" one ": [1, 2], " two ": [3, 4]})
        ds.df = df1
        ds.strip_cols()
        df2 = pl.DataFrame({"one": [1, 2], "two": [3, 4]})
        assert_frame_equal(ds.df, df2)

    def test_roundvals(self):
        df1 = pl.DataFrame({"one": [1.345854, 2.1], "two": [3.0, 4.0]})
        ds.df = df1
        ds.roundvals("one")
        df2 = pl.DataFrame({"one": [1.35, 2.1], "two": [3.0, 4.0]})
        assert_frame_equal(ds.df, df2)
        with pytest.raises(pl.ColumnNotFoundError):
            ds.df = df1
            ds.roundvals("wrong")

    def test_fdates(self):
        # iso format
        ds.df = pl.DataFrame(
            {"one": ["val1", "val2"], "two": ["2002/12/01", "2003/12/02"]}
        )
        ds.to_date("two", fmt="%Y/%m/%d")
        base_df = ds.df.clone()
        print("DT", ds.df["two"].dtype)
        ds.fdate("two")
        ds.drop("two")
        df2 = pl.DataFrame(
            {
                "one": ["val1", "val2"],
                "fdate": ["2002-12-01 00:00:00", "2003-12-02 00:00:00"],
            },
        )
        assert_frame_equal(ds.df, df2)
        # year only
        ds.df = base_df
        ds.fdate("two", precision="Y")
        ds.drop("two")
        df2 = pl.DataFrame({"one": ["val1", "val2"], "fdate": ["2002", "2003"]})
        assert_frame_equal(ds.df, df2)
        # year month
        ds.df = base_df
        ds.fdate("two", precision="M")
        ds.drop("two")
        df2 = pl.DataFrame({"one": ["val1", "val2"], "fdate": ["2002-12", "2003-12"]})
        assert_frame_equal(ds.df, df2)
        # year month day
        ds.df = base_df
        df2 = pl.DataFrame(
            {"one": ["val1", "val2"], "fdate": ["2002-12-01", "2003-12-02"]}
        )
        ds.fdate("two", precision="D")
        ds.drop("two")
        assert_frame_equal(ds.df, df2)
        # year month day hour
        ds.df = base_df
        df2 = pl.DataFrame(
            {"one": ["val1", "val2"], "fdate": ["2002-12-01 00", "2003-12-02 00"]}
        )
        ds.fdate("two", precision="H")
        ds.drop("two")
        assert_frame_equal(ds.df, df2)
        # year month day hour minute
        ds.df = base_df
        df2 = pl.DataFrame(
            {"one": ["val1", "val2"], "fdate": ["2002-12-01 00:00", "2003-12-02 00:00"]}
        )
        ds.fdate("two", precision="Min")
        ds.drop("two")
        assert_frame_equal(ds.df, df2)
        # year month day hour minute second
        ds.df = base_df
        df2 = pl.DataFrame(
            {
                "one": ["val1", "val2"],
                "fdate": ["2002-12-01 00:00:00", "2003-12-02 00:00:00"],
            }
        )
        ds.fdate("two", precision="S")
        ds.drop("two")
        assert_frame_equal(ds.df, df2)

    def test_nulls(self):
        ds.df = pl.DataFrame({"one": ["val1", "val2"], "two": ["", None]})
        ds.fill_nulls("two", val="xxx")
        df2 = pl.DataFrame({"one": ["val1", "val2"], "two": ["", "xxx"]})
        assert_frame_equal(ds.df, df2)
        ds.df = pl.DataFrame({"one": ["val1", "val2"], "two": [None, None]})
        ds.fill_nulls(val="xxx")
        df2 = pl.DataFrame({"one": ["val1", "val2"], "two": ["xxx", "xxx"]})
        assert_frame_equal(ds.df, df2)
