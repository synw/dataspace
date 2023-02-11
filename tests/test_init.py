import dataspace
import pandas as pd
from pandas.testing import assert_frame_equal

from tests.base import BaseDsTest


class TestDsDataInit(BaseDsTest):
    def test_load_csv(self):
        df = pd.DataFrame({"one": [1], "two": [2]})
        ds = dataspace.from_csv(self.path + "/fixtures/data.csv")
        assert_frame_equal(ds.df, df)
