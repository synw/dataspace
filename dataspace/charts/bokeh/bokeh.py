from typing import Dict, List, Optional, Union
import pandas as pd
import holoviews as hv
from holoviews.core.data.interface import DataError
from dataspace.charts.bokeh.charts import (
    Bars,
    Curve,
    # HLine,
    Scatter,
    Area,
    Histogram,
    HeatMap,
)

hv.extension("bokeh")


class BokehChart:
    x = None
    y = None
    default_width: int
    default_height: int = 0

    def __init__(self, default_width: int) -> None:
        self.default_width = default_width

    def chart(
        self,
        df: pd.DataFrame,
        chart_type,
        x: Optional[Union[str, List[str]]] = None,
        y: Optional[Union[str, List[str]]] = None,
        **kwargs,
    ):
        """
        Get a Bokeh chart object
        """
        if x is not None and y is not None:
            self.set_axis(x, y)
        else:
            self._checkAxis()
        args = {}
        args["data"] = df
        args["kdims"] = self.x
        args["vdims"] = self.y
        opts = self._default_opts(kwargs)
        chart = None
        try:
            if chart_type == "line":
                chart = Curve(**args)
            elif chart_type == "hline":
                chart = hv.HLine(float(df[self.y].mean()))
            elif chart_type == "point":
                chart = Scatter(**args)
            elif chart_type == "area":
                chart = Area(**args)
            elif chart_type == "bar":
                chart = Bars(**args)
            elif chart_type == "hist":
                chart = Histogram(**args)
            # elif chart_type == "errorBar":
            #    chart = hv.ErrorBars(**args)
            elif chart_type == "heatmap":
                chart = HeatMap(**args)
            # elif chart_type == "lreg":
            #    chart = self._lreg_bokeh(**args)
            elif chart_type == "sline":
                # window_size, y_label = (options["window_size"],)
                # options["y_label"]
                # chart = self._sline_bokeh(window_size, y_label)
                pass
            if chart is None:
                raise Exception("Chart type " + chart_type + " unknown")
            return chart.opts(**opts)
        except DataError as e:
            msg = f"Column not found in ${self.x} and ${self.y}"
            raise Exception(msg, e)
        except Exception as e:
            raise e

    def set_axis(
        self, xaxis: Union[str, List[str]], yaxis: Union[str, List[str]]
    ) -> None:
        if isinstance(xaxis, list):
            self.x = xaxis
        else:
            self.x = [xaxis]
        if isinstance(yaxis, list):
            self.y = yaxis
        else:
            self.y = [yaxis]

    def _checkAxis(self):
        assert self.x is not None or self.y is not None, "Set the chart fields"

    def _default_opts(self, opts: Dict):
        if "width" not in opts:
            opts["width"] = self.default_width
        if "height" not in opts:
            if self.default_height > 0:
                opts["height"] = self.default_height
        if "color" not in opts:
            opts["color"] = "#30A2DA"
        return opts
