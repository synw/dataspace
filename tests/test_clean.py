import pytest
import datetime
import pandas as pd
import numpy as np
import dataspace
from pandas.testing import assert_frame_equal

from tests.base import BaseDsTest

ds = dataspace.from_df(pd.DataFrame())


class TestDsDataClean(BaseDsTest):
    def test_drop_nan(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": ["two", np.nan]})
        ds.df = df1
        ds.drop_nan("two")
        df2 = pd.DataFrame({"one": ["one"], "two": ["two"]})
        assert_frame_equal(ds.df, df2)
        ds.df = df1
        ds.drop_nan(how="any")
        assert_frame_equal(ds.df, df2)
        ds.df = df1
        ds.drop_nan(["two"])
        assert_frame_equal(ds.df, df2)

    def test_fill_nan(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": ["two", None]}, ["1", "2"])
        ds.df = df1
        ds.fill_nan("two", "two")
        df2 = pd.DataFrame({"one": ["one", "two"], "two": ["two", "two"]}, ["1", "2"])
        assert_frame_equal(ds.df, df2)

    def test_replace(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": ["two", "two"]}, ["1", "2"])
        ds.df = df1
        ds.replace("one", "two", "three")
        df2 = pd.DataFrame({"one": ["one", "three"], "two": ["two", "two"]}, ["1", "2"])
        assert_frame_equal(ds.df, df2)

    def test_to_int(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": [1.0, 2.0]}, ["1", "2"])
        ds.df = df1
        ds.to_int("two")
        self.assertEqual(list(ds.df["two"]), [1, 2])
        with pytest.raises(ValueError):
            ds.df = pd.DataFrame(
                {"one": ["one", "two"], "two": ["wrong", 2.0]}, ["1", "2"]
            )
            ds.to_int("two")

    def test_to_float(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": [1, 2]}, ["1", "2"])
        ds.df = df1
        ds.to_float("two")
        self.assertEqual(list(ds.df["two"]), [1.0, 2.0])
        with pytest.raises(ValueError):
            ds.df = pd.DataFrame({"one": ["one", "two"], "two": ["wrong", 2]})
            ds.to_float("two")

    def test_to_type(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": [1, 2]})
        ds.df = df1
        ds.to_type(str, "two")
        df2 = pd.DataFrame({"one": ["one", "two"], "two": ["1", "2"]})
        df2.astype(str, "two")
        assert_frame_equal(ds.df, df2)
        with pytest.raises(ValueError):
            ds.df = pd.DataFrame(
                {"one": ["one", "two"], "two": ["wrong", 2.0]}, ["1", "2"]
            )
            ds.to_type(int, "two")
        with pytest.raises(ValueError):
            ds.to_type(str, "wrongcol")

    """def tests_timestamps(self):
        df1 = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2002/12/02"]}, [1, 2]
        )
        ds.df = df1
        ds.timestamps("two", name="ts")
        df2 = pd.DataFrame(
            {
                "one": ["one", "two"],
                "ts": [1038700800, 1038787200],
                "two": ["2002/12/01", "2002/12/02"],
            },
            [1, 2],
        )
        ds.df = ds.df.reindex(sorted(ds.df.columns), axis=1)
        assert_frame_equal(ds.df, df2)
        ds.df = df1
        ds.timestamps("two")
        with pytest.raises(ValueError):
            ds.timestamps("two", unit="s", errors="raise")

    def test_date_index(self):
        df1 = pd.DataFrame(
            {"one": ["one", "two"], "date": ["2002/12/01", "2002/12/02"]}, [1, 2]
        )
        ds.df = df1
        ds.dateindex("date")
        index = np.array(
            ["2002-12-01T00:00:00.000000000", "2002-12-02T00:00:00.000000000"],
            dtype="datetime64[ns]",
        )
        np.testing.assert_array_equal(ds.df.index.values, index)
        ds.df = None
        ds.dateindex("date")
        self.assertRaises(TypeError)
        ds.dateindex("wrong")
        self.assertRaises(TypeError)

    def test_index(self):
        df1 = pd.DataFrame([[1, 3], [2, 4]], columns=["one", "two"])
        ds.df = df1
        ds.index("one")
        index = np.array([1, 2])
        np.testing.assert_array_equal(ds.df.index.values, index)
        ds.df = None
        ds.index("one")
        self.assertRaises(TypeError)

    def test_strip(self):
        df = pd.DataFrame({"one": [" 2 ", "1 ", "0 "], "two": [2, 1, 1]})
        ds.df = df
        ds.strip("one")
        df2 = pd.DataFrame({"one": ["2", "1", "0"], "two": [2, 1, 1]})
        assert_frame_equal(ds.df, df2)
        ds.df = None
        ds.strip("one")
        self.assertRaises(TypeError)
        ds.df = "wrong"
        ds.index("one")
        self.assertRaises(AttributeError)

    def test_strip_cols(self):
        df1 = pd.DataFrame([[1, 3], [2, 4]], columns=[" one ", " two "])
        ds.df = df1
        ds.strip_cols()
        df2 = pd.DataFrame([[1, 3], [2, 4]], columns=["one", "two"])
        assert_frame_equal(ds.df, df2)
        ds.df = pd.DataFrame([[1, 3], [2, 4]], columns=["one", None])
        ds.strip_cols()

    def test_roundvals(self):
        df1 = pd.DataFrame([[1.345854, 3.0], [2.1, 4.0]], columns=["one", "two"])
        ds.df = df1
        ds.roundvals("one")
        df2 = pd.DataFrame([[1.35, 3.0], [2.1, 4.0]], columns=["one", "two"])
        assert_frame_equal(ds.df, df2)
        ds.df = df1
        ds.roundvals("wrong")
        self.assertRaises(KeyError)

    def test_format_date(self):
        date = datetime.datetime(2011, 1, 3, 0, 0)
        d2 = ds.format_date_(date)
        self.assertEqual(d2, "2011-01-03 00:00:00")

    def test_date(self):
        df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2003/12/02"]}, [1, 2]
        )
        ds.df = df
        ds.date("two")
        self.assertEqual(ds.df.two.dtype, "datetime64[ns]")
        # self.assertErr("ValueError", ds.date, "one")

    def test_fdates(self):
        ds.df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2003/12/02"]}, [1, 2]
        )
        ds.fdate("two")
        df2 = pd.DataFrame(
            {
                "one": ["one", "two"],
                "two": ["2002-12-01 00:00:00", "2003-12-02 00:00:00"],
            },
            [1, 2],
        )
        assert_frame_equal(ds.df, df2)

        ds.df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2003/12/02"]}, [1, 2]
        )
        df2 = pd.DataFrame({"one": ["one", "two"], "two": ["2002", "2003"]}, [1, 2])
        ds.fdate("two", precision="Y")
        assert_frame_equal(ds.df, df2)

        ds.df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2003/12/02"]}, [1, 2]
        )
        df2 = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002-12", "2003-12"]}, [1, 2]
        )
        ds.fdate("two", precision="M")
        assert_frame_equal(ds.df, df2)

        ds.df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2003/12/02"]}, [1, 2]
        )
        df2 = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002-12-01", "2003-12-02"]}, [1, 2]
        )
        ds.fdate("two", precision="D")
        assert_frame_equal(ds.df, df2)

        ds.df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2003/12/02"]}, [1, 2]
        )
        df2 = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002-12-01 00", "2003-12-02 00"]}, [1, 2]
        )
        ds.fdate("two", precision="H")
        assert_frame_equal(ds.df, df2)

        ds.df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2003/12/02"]}, [1, 2]
        )
        df2 = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002-12-01 00:00", "2003-12-02 00:00"]},
            [1, 2],
        )
        ds.fdate("two", precision="Min")
        assert_frame_equal(ds.df, df2)

        ds.df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2003/12/02"]}, [1, 2]
        )
        df2 = pd.DataFrame({"one": ["one", "two"], "two": ["2002", "2003"]}, [1, 2])
        ds.fdate("two", format="%Y")
        assert_frame_equal(ds.df, df2)

        ds.df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "2003/12/02"]}, [1, 2]
        )
        ds.fdate("wrong")
        self.assertRaises(KeyError)

        ds.df = pd.DataFrame(
            {"one": ["one", "two"], "two": ["2002/12/01", "wrong"]}, [1, 2]
        )
        ds.fdate("two", "wrong")
        self.assertRaises(TypeError)

        ds.df = None
        ds.fdate("two")
        self.assertRaises(ValueError)

    def test_nulls(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": ["", None]}, ["1", "2"])
        ds.df = df1
        ds.fill_nulls("two")
        df2 = pd.DataFrame({"one": ["one", "two"], "two": [nan, nan]}, ["1", "2"])
        assert_frame_equal(ds.df, df2)
        ds.df = None
        ds.fill_nulls("two")
        self.assertRaises(AttributeError)

    def test_nan_empty(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": ["two", ""]}, ["1", "2"])
        ds.df = df1
        ds.nan_empty("two")
        df2 = pd.DataFrame({"one": ["one", "two"], "two": ["two", nan]}, ["1", "2"])
        assert_frame_equal(ds.df, df2)
        ds.df = None
        ds.nan_empty("two")
        self.assertRaises(TypeError)"""
