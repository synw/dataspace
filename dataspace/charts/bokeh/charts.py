from typing import List, Union
import holoviews as hv
from holoviews.core import Store
from holoviews.element import Chart, Annotation
from holoviews.plotting import bokeh as plot
from bokeh.models import HoverTool


class HvChart(Chart):
    def w(self, v: int):
        self.opts(width=v)
        return self

    def h(self, v: int):
        self.opts(height=v)
        return self

    def color(self, v: str):
        return self.opts(color=v)

    def opacity(self, v: str):
        return self.opts(alpha=v)

    def tooltip(self, v: Union[str, List[str]]):
        t = []
        if isinstance(v, str) is True:
            t = [v]
        else:
            t = v
        tt = []
        for x in t:
            tt.append((x, x))
        hover = HoverTool(tooltips=tt)
        return self.opts(tools=[hover])


class HvAnnotation(Annotation):
    def w(self, v: int):
        self.opts(width=v)
        return self

    def h(self, v: int):
        self.opts(height=v)
        return self

    def color(self, v: str):
        return self.opts(color=v)

    def opacity(self, v: str):
        return self.opts(alpha=v)


class Bars(hv.Bars, HvChart):
    def __init__(self, *args, **kwargs):
        super(hv.Bars, self).__init__(*args, **kwargs)


class Curve(hv.Curve, HvChart):
    def __init__(self, *args, **kwargs):
        super(hv.Curve, self).__init__(*args, **kwargs)


class HLine(hv.HLine, HvAnnotation):
    def __init__(self, *args, **kwargs):
        super(hv.HLine, self).__init__(*args, **kwargs)


class Scatter(hv.Scatter, HvChart):
    def __init__(self, *args, **kwargs):
        super(hv.Scatter, self).__init__(*args, **kwargs)


class Area(hv.Area, HvChart):
    def __init__(self, *args, **kwargs):
        super(hv.Area, self).__init__(*args, **kwargs)


class Histogram(hv.Histogram, HvChart):
    def __init__(self, *args, **kwargs):
        super(hv.Histogram, self).__init__(*args, **kwargs)


class HeatMap(hv.HeatMap, HvChart):
    def __init__(self, *args, **kwargs):
        super(hv.HeatMap, self).__init__(*args, **kwargs)


Store.register(
    {
        Bars: plot.BarPlot,
        Curve: plot.CurvePlot,
        HLine: plot.VectorFieldPlot,
        Scatter: plot.PointPlot,
        Area: plot.AreaPlot,
        Histogram: plot.HistogramPlot,
        HeatMap: plot.HeatMapPlot,
    },
    "bokeh",
)
