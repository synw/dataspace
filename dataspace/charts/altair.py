from typing import Dict
import numpy as np
import pandas as pd
from altair import Chart, X, Y, Scale, data_transformers

from dataspace.transform import _drop
from dataspace.core.env import is_notebook

data_transformers.disable_max_rows()


class AltairChart:
    x = None
    y = None
    default_width: int = None

    def __init__(self, default_width: int) -> None:
        self.default_width = default_width
        """if is_notebook is True:
            try:
                renderers.enable("notebook")
            except Exception:
                pass"""

    def chart(
        self, df: pd.DataFrame, chart_type, opts={}, style={}, encode={}
    ) -> Chart:
        """
        Get an Altair chart object
        """
        self._checkAxis()
        opts = self._default_opts(opts)
        chart = None
        if chart_type == "bar":
            chart = (
                Chart(df)
                .mark_bar(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "circle":
            chart = (
                Chart(df)
                .mark_circle(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "line":
            chart = (
                Chart(df)
                .mark_line(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "hline":
            chart = self._altair_hline_(df, opts, style, encode)
        elif chart_type == "line_num":
            chart = self._altair_chart_num_(df, "line", opts, style, encode)
        elif chart_type == "bar_num":
            chart = self._altair_chart_num_(df, "bar", opts, style, encode)
        elif chart_type == "point_num":
            chart = self._altair_chart_num_(df, "point", opts, style, encode)
        elif chart_type == "point":
            chart = (
                Chart(df)
                .mark_point(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "area":
            chart = (
                Chart(df)
                .mark_area(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "heatmap":
            chart = (
                Chart(df)
                .mark_rect(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "text":
            chart = (
                Chart(df)
                .mark_text(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "square":
            chart = (
                Chart(df)
                .mark_square(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "tick":
            chart = (
                Chart(df)
                .mark_tick(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "rule":
            chart = (
                Chart(df)
                .mark_rule(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        return chart

    def _altair_chart_num_(
        self,
        df: pd.DataFrame,
        chart_type: str,
        opts,
        style,
        encode,
    ) -> Chart:
        """
        Get a chart + text number chart
        """
        if chart_type == "line":
            c = (
                Chart(df)
                .mark_line(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "bar":
            c = (
                Chart(df)
                .mark_bar(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        elif chart_type == "point":
            c = (
                Chart(df)
                .mark_point(**style)
                .encode(x=self.x, y=self.y, **encode)
                .properties(**opts)
            )
        encoder = encode
        if "text" not in encoder:
            encoder["text"] = self.y
        if "align" not in style:
            style["align"] = "center"
        if "dy" not in style:
            style["dy"] = -5
        if "dx" not in style and chart_type != "bar":
            style["dx"] = 8
        if "size" in style:
            del style["size"]
        # style["color"] = text_color
        # df2 = df.replace({self.y.split(":")[0]: {0: np.nan}})
        num = (
            Chart(df)
            .mark_text(**style)
            .encode(x=self.x, y=self.y, **encoder)
            .properties(**opts)
        )
        return c + num

    def _altair_hline_(self, df: pd.DataFrame, opts, style, encode) -> Chart:
        """
        Get a mean line chart
        """
        try:
            rawy = self.y.shorthand
            if ":" in self.y.shorthand:
                rawy = self.y.shorthand.split(":")[0]
            mean = df[rawy].mean()
            lx = []
            i = 0
            while i < len(df[rawy]):
                lx.append(mean)
                i += 1
            df["Mean"] = lx
            chart = (
                Chart(df)
                .mark_line(**style)
                .encode(x=self.x, y="Mean:Q", **encode)
                .properties(**opts)
            )
            _drop(df, "Mean")
            return chart
        except Exception as e:
            raise Exception("Can not draw mean line chart", e)

    def set_axis(self, xaxis: str, yaxis: str) -> None:
        self.x = X(xaxis, scale=Scale(zero=False))
        self.y = Y(yaxis, scale=Scale(zero=False))

    def _checkAxis(self):
        assert self.x is not None and self.y is not None, "Set the chart fields"

    def _default_opts(self, opts: Dict):
        if "width" not in opts:
            opts["width"] = self.default_width
        return opts
