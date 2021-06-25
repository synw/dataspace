import pandas as pd
from altair import Chart
from .altair import AltairChart
from .bokeh import BokehChart


class DsChart:
    engine = "bokeh"
    default_width = 950
    altair: AltairChart = None
    bokeh: BokehChart = None

    def set_axis(self, x_axis_col: str, y_axis_col: str):
        self._check_engine()
        if self.engine == "altair":
            return self.altair.set_axis(x_axis_col, y_axis_col)
        elif self.engine == "bokeh":
            return self.bokeh.set_axis(x_axis_col, y_axis_col)

    def chart(self, df: pd.DataFrame, chart_type, **kwargs):
        self._check_engine()
        if self.engine == "altair":
            return self.altair.chart(df, chart_type, **kwargs)
        elif self.engine == "bokeh":
            return self.bokeh.chart(df, chart_type, **kwargs)

    def _check_engine(self):
        if self.engine == "altair":
            if self.altair is None:
                self.altair = AltairChart(self.default_width)
        elif self.engine == "bokeh":
            if self.bokeh is None:
                self.bokeh = BokehChart(self.default_width)
