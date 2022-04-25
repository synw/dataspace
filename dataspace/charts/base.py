import pandas as pd
from .altair import AltairChart
from .bokeh import BokehChart


class DsChart:
    engine = "altair"
    altair: AltairChart
    bokeh: BokehChart

    def __init__(self, engine="bokeh", default_width=950) -> None:
        self.engine = engine
        self.altair = AltairChart(default_width)
        self.bokeh = BokehChart(default_width)

    def set_axis(self, x_axis_col: str, y_axis_col: str):
        if self.engine == "altair":
            return self.altair.set_axis(x_axis_col, y_axis_col)
        elif self.engine == "bokeh":
            return self.bokeh.set_axis(x_axis_col, y_axis_col)

    def chart(self, df: pd.DataFrame, chart_type, **kwargs):
        if self.engine == "altair":
            return self.altair.chart(df, chart_type, **kwargs)
        elif self.engine == "bokeh":
            return self.bokeh.chart(df, chart_type, **kwargs)

    def width(self, v: int):
        self.altair.default_width = v
        self.bokeh.default_width = v

    def height(self, v: int):
        self.altair.default_height = v
        self.bokeh.default_height = v

    def wh(self, w: int, h: int):
        self.width(w)
        self.height(h)
