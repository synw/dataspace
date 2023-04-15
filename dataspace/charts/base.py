from ctypes import ArgumentError

from .altair import AltairChartEngine

from dataspace.types import ChartEngineName, ChartType

try:
    from .bokeh import BokehChartEngine  # type: ignore
except (ModuleNotFoundError, ImportError):
    # print("The Bokeh chart engine is not available in this environment")
    pass

    class BokehChartEngine(AltairChartEngine):
        pass


class DsChartEngine:
    engine: ChartEngineName = "altair"
    altair: AltairChartEngine
    bokeh: BokehChartEngine

    def __init__(self, engine: ChartEngineName = "altair", default_width=950) -> None:
        self.engine = engine
        self.altair = AltairChartEngine(default_width)
        self.bokeh = BokehChartEngine(default_width)

    def set_axis(self, x_axis_col: str, y_axis_col: str):
        if self.engine == "altair":
            self.altair.set_axis(x_axis_col, y_axis_col)
        elif self.engine == "bokeh":
            self.bokeh.set_axis(x_axis_col, y_axis_col)

    def chart(self, *args, **kwargs) -> ChartType:
        if "df" in kwargs.keys():
            del kwargs["df"]
        chart_type: str = args[1]
        df = args[0]
        x = None
        y = None
        if len(args) > 2:
            if len(args) != 4:
                raise ArgumentError("Provide arguments for x and y axis")
            x = args[2]
            y = args[3]
        chart: ChartType
        if self.engine == "altair":
            chart = self.altair.chart(df, chart_type, x, y, **kwargs)
            # if is_running_in_browser is True:
            #    return c.to_json()
        else:
            chart = self.bokeh.chart(df, chart_type, x, y, **kwargs)
        return chart

    def width(self, v: int):
        self.altair.default_width = v
        self.bokeh.default_width = v

    def height(self, v: int):
        self.altair.default_height = v
        self.bokeh.default_height = v

    def wh(self, w: int, h: int):
        self.width(w)
        self.height(h)

    """def save_img(self, chart, path):
        if self.engine == "bokeh":
            self.bokeh.save_img(chart, path)"""
