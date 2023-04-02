import dataspace
import polars as pl
from polars.testing import assert_frame_equal

from tests.base import BaseDsTest


class TestDsDataInit(BaseDsTest):
    def test_load_csv(self):
        df = pl.DataFrame({"one": [1], "two": [2]})
        ds = dataspace.from_csv(self.path + "/fixtures/data.csv")
        assert_frame_equal(ds.df, df)
