from ctypes import ArgumentError
from typing import Literal

import pandas as pd

from .altair import AltairChart

# from dataspace.core.env import is_running_in_browser

try:
    from .bokeh import BokehChart
except (ModuleNotFoundError, ImportError):
    print("The Bokeh chart engine is not available in this environment")

    class BokehChart(AltairChart):
        pass


class DsChart:
    engine: Literal["altair", "bokeh"] = "altair"
    altair: AltairChart
    bokeh: BokehChart

    def __init__(self, engine="altair", default_width=950) -> None:
        self.engine = engine
        self.altair = AltairChart(default_width)
        self.bokeh = BokehChart(default_width)

    def set_axis(self, x_axis_col: str, y_axis_col: str):
        if self.engine == "altair":
            return self.altair.set_axis(x_axis_col, y_axis_col)
        elif self.engine == "bokeh":
            return self.bokeh.set_axis(x_axis_col, y_axis_col)

    def chart(self, *args, **kwargs):
        if "df" in kwargs.keys():
            del kwargs["df"]
        chart_type: str = args[1]
        df: pd.DataFrame = args[0]
        x = None
        y = None
        if len(args) > 2:
            if len(args) != 4:
                raise ArgumentError("Provide arguments for x and y axis")
            x = args[2]
            y = args[3]
        if self.engine == "altair":
            c = self.altair.chart(df, chart_type, x, y, **kwargs)
            # if is_running_in_browser is True:
            #    return c.to_json()
            return c
        elif self.engine == "bokeh":
            return self.bokeh.chart(df, chart_type, x, y, **kwargs)

    def width(self, v: int):
        self.altair.default_width = v
        self.bokeh.default_width = v

    def height(self, v: int):
        self.altair.default_height = v
        self.bokeh.default_height = v

    def wh(self, w: int, h: int):
        self.width(w)
        self.height(h)
