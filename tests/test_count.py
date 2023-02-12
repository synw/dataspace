import pytest
import pandas as pd
import dataspace

from tests.base import BaseDsTest

ds = dataspace.from_df(pd.DataFrame())


class TestDsDataCount(BaseDsTest):
    def test_count_nulls(self):
        ds.df = pd.DataFrame({"one": None, "two": 2}, ["1", "2"])
        msg = "Found 2 nulls in column one"
        self.assertOk(msg, ds.count_null_, "one")
        msg = "Can not find column wrong"
        with pytest.raises(KeyError):
            ds.count_null_("wrong")

    def test_count_empty(self):
        ds.df = pd.DataFrame({"one": "", "two": 2}, ["1", "2"])
        msg = "Found 2 empty rows in column one"
        self.assertOk(msg, ds.count_empty_, "one")
        with pytest.raises(KeyError):
            ds.count_empty_("wrong")

    def test_count_zero(self):
        ds.df = pd.DataFrame({"one": 0, "two": 2}, ["1", "2"])
        msg = "Found 2 zero values in column one"
        self.assertOk(msg, ds.count_zero_, "one")
        with pytest.raises(KeyError):
            ds.count_zero_("wrong")

    def test_count_unique(self):
        ds.df = pd.DataFrame({"one": [0, 0, 1], "two": [2, 1, 1]})
        msg = "Found 2 unique values in column one"
        self.assertOk(msg, ds.count_unique_, "one")
        with pytest.raises(KeyError):
            ds.count_unique_("wrong")
