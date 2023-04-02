import pytest
import polars as pl
import dataspace

from tests.base import BaseDsTest

ds = dataspace.from_df(pl.DataFrame())


class TestDsDataCount(BaseDsTest):
    def test_count_nulls(self):
        ds.df = pl.DataFrame({"one": [None, None], "two": [1, 2]})
        ds.count_null_("one")
        msg = "Found 2 nulls in column one"
        self.assertOk(msg, ds.count_null_, "one")
        with pytest.raises(pl.ColumnNotFoundError):
            ds.count_null_("wrong")

    def test_count_empty(self):
        ds.df = pl.DataFrame({"one": ["", ""], "two": [1, 2]})
        msg = "Found 2 empty rows in column one"
        self.assertOk(msg, ds.count_empty_, "one")
        with pytest.raises(pl.ColumnNotFoundError):
            ds.count_empty_("wrong")

    def test_count_zero(self):
        ds.df = pl.DataFrame({"one": [0, 0], "two": [1, 2]})
        msg = "Found 2 rows with 0 value in column one"
        self.assertOk(msg, ds.count_zero_, "one")
        with pytest.raises(pl.ColumnNotFoundError):
            ds.count_zero_("wrong")

    def test_count_unique(self):
        ds.df = pl.DataFrame({"one": ["val1", "val2"], "two": [0, 0]})
        msg = "Found 2 unique values in column one"
        self.assertOk(msg, ds.count_unique_, "one")
        with pytest.raises(pl.ColumnNotFoundError):
            ds.count_unique_("wrong")
