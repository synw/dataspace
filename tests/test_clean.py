import pytest
import polars as pl
import numpy as np
import dataspace
from polars.testing import assert_frame_equal

from tests.base import BaseDsTest

ds = dataspace.from_df(pl.DataFrame())


class TestDsDataClean(BaseDsTest):
    def test_drop_nan(self):
        df1 = pl.DataFrame(
            {"one": pl.Series(["one", "two"]), "two": pl.Series([None, None])}
        )
        ds.df = df1
        ds.drop_all_nulls()
        df2 = pl.DataFrame({"one": pl.Series(["one", "two"])})
        assert_frame_equal(ds.df, df2)
        ds.df = pl.DataFrame(
            {"one": pl.Series(["one", "two"]), "two": pl.Series([None, "x"])}
        )
        ds.drop_any_nulls("one")
        assert_frame_equal(ds.df, df2)

    def test_replace(self):
        df1 = pl.DataFrame(
            {"one": pl.Series(["one", "two"]), "two": pl.Series(["two", "two"])}
        )
        ds.df = df1
        ds.replace("one", "two", "three")
        df2 = pl.DataFrame(
            {"one": pl.Series(["one", "three"]), "two": pl.Series(["two", "two"])}
        )
        assert_frame_equal(ds.df, df2)

    def test_to_int(self):
        df1 = pl.DataFrame({"one": ["one", "two"], "two": [1.0, 2.0]})
        ds.df = df1
        ds.to_int("two")
        self.assertEqual(list(ds.df["two"]), [1, 2])
        with pytest.raises(ValueError):
            ds.df = pl.DataFrame({"one": ["one", "two"], "two": ["wrong", 2.0]})
            ds.to_int("two")

    def test_to_float(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": [1, 2]}, ["1", "2"])
        ds.df = df1
        ds.to_float("two")
        self.assertEqual(list(ds.df["two"]), [1.0, 2.0])
        with pytest.raises(ValueError):
            ds.df = pl.DataFrame({"one": ["one", "two"], "two": ["wrong", 2]})
            ds.to_float("two")

    def test_to_type(self):
        df1 = pl.DataFrame({"one": ["one", "two"], "two": [1, 2]})
        ds.df = df1
        ds.to_type(pl.Utf8, "two")  # type: ignore
        df2 = pl.DataFrame({"one": ["one", "two"], "two": ["1", "2"]})
        df2.astype(str, "two")
        assert_frame_equal(ds.df, df2)
        with pytest.raises(ValueError):
            ds.df = pd.DataFrame(
                {"one": ["one", "two"], "two": ["wrong", 2.0]}, ["1", "2"]
            )
            ds.to_type(pl.Int64, "two")  # type: ignore
        with pytest.raises(ValueError):
            ds.to_type(pl.Utf8, "wrongcol")  # type: ignore

    def tests_timestamps(self):
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
        with pytest.raises(KeyError):
            ds.dateindex("wrong")

    def test_index(self):
        df1 = pd.DataFrame([[1, 3], [2, 4]], columns=["one", "two"])
        ds.df = df1
        ds.index("one")
        index = np.array([1, 2])
        np.testing.assert_array_equal(ds.df.index.values, index)

    def test_strip(self):
        df = pd.DataFrame({"one": [" 2 ", "1 ", "0 "], "two": [2, 1, 1]})
        ds.df = df
        ds.strip("one")
        df2 = pd.DataFrame({"one": ["2", "1", "0"], "two": [2, 1, 1]})
        assert_frame_equal(ds.df, df2)

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
        with pytest.raises(KeyError):
            ds.df = df1
            ds.roundvals("wrong")

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

    def test_nulls(self):
        df1 = pd.DataFrame({"one": ["one", "two"], "two": ["", None]}, ["1", "2"])
        ds.df = df1
        ds.fill_nulls("two")
        df2 = pd.DataFrame({"one": ["one", "two"], "two": [np.nan, np.nan]}, ["1", "2"])
        assert_frame_equal(ds.df, df2)
        ds.df = df1
        ds.fill_nulls()
        assert_frame_equal(ds.df, df2)
