from ctypes import ArgumentError
from typing import Dict, List, Optional, Union

import pandas as pd
from dataspace.transform import _drop

from altair import Chart as AltChart
from altair import Color, Scale, X, Y, data_transformers, value

data_transformers.disable_max_rows()


class Chart(AltChart):
    def w(self, v: int) -> "Chart":
        """Set the width of the chart

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.line_().w(500).to_json()

        :param v: value in pixels
        :type v: int
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(width=v)

    def h(self, v: int) -> "Chart":
        """Set the height of the chart

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.line_().h(200).to_json()

        :param v: value in pixels
        :type v: int
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(height=v)

    def wh(self, w: int, h: int) -> "Chart":
        """Set the width and height of a chart

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.line_().wh(500, 200).to_json()

        :param w: width value in pixels
        :type w: int
        :param h: height value in pixels
        :type h: int
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(width=w, height=h)

    def mw(self, v: int) -> "Chart":
        """Configure the default mark width

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.bar_().mw(7).to_json()

        :param v: width value in pixels
        :type v: int
        :return: the chart object
        :rtype: Chart
        """
        return self.configure_mark(width=v)

    def pw(self, v: int) -> "Chart":
        """Configure the default point width

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.point_().pw(25).to_json()

        :param v: width value in pixels
        :type v: int
        :return: the chart object
        :rtype: Chart
        """
        return self.configure_point(size=v)

    def color(self, v: str) -> "Chart":
        """Configure the chart color

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.area_().color("forestgreen").to_json()

        :param v: the color value
        :type v: str
        :return: the chart object
        :rtype: Chart
        """
        return self.configure_mark(color=v)

    def opacity(self, v: Union[int, float]) -> "Chart":
        """Configure the chart opacity

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.point_().opacity(0.5).to_json()

        :param v: the opacity value
        :type v: Union[int, float]
        :return: the chart object
        :rtype: Chart
        """
        return self.encode(opacity=value(v))

    def tooltip(self, v: Union[str, List[str]]) -> "Chart":
        """Configure a tooltip on hover for some colums

        The tooltip shows up when the user cursor goes
        over the datapoint on the chart

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.point_("date:T", "price:Q").tooltip(["date","price"]).to_json()

        :param v: column or list of columns to use for the tooltip
        :type v: Union[str, List[str]]
        :return: the chart object
        :rtype: Chart
        """
        return self.encode(tooltip=v)

    def to(self, v: str) -> "Chart":
        """Change the chart type for an existing chart (only for the Altair engine)

        :param v: the new chart type
        :type v: str
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(mark=v)

    def rx(self, v=-45) -> "Chart":
        """Rotate the chart x labels

        :param v: angle of rotation to use, defaults to -45
        :type v: int, optional
        :return: the chart object
        :rtype: Chart
        """
        self.encoding.x.axis.labelAngle = v
        return self

    def nox(self) -> "Chart":
        """Remove the x axis labels

        .. code-block:: python

            ds = await load_dataset("timeserie")
            ds.axis("date:T", "data:Q")
            (ds.line_().nox() + ds.point_().nox()).to_json()

        :return: the chart object
        :rtype: Chart
        """
        self.encoding.x.axis = None
        return self

    def noy(self) -> "Chart":
        """Remove the y axis labels

        .. code-block:: python

            ds = await load_dataset("timeserie")
            ds.axis("date:T", "data:Q")
            (ds.line_().noy() + ds.point_().noy()).to_json()

        :return: the chart object
        :rtype: Chart
        """
        self.encoding.y.axis = None
        return self

    def title(self, v: str) -> "Chart":
        """Add a text title to the chart

        .. code-block:: python

            ds = await load_dataset("timeserie")
            ds.area_("date:T", "data:Q").title("The chart title").to_json()


        :param v: the title text
        :type v: str
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(title=v)

    def colormap(self, column: str, **kwargs) -> "Chart":
        """Add a values based colormap to the chart

        :param column: the column to use
        :type column: str
        :param kwargs: the colors and values map to use
        :type kwargs: Dict[str,str]
        :raises ArgumentError: raised if less than two colors are provided
        :return: the chart object
        :rtype: Chart
        """
        if len(kwargs) < 2:
            raise ArgumentError("Provide at least two colors in the map")
        levels: List = []
        colors: List[str] = []
        for kw in kwargs.keys():
            levels.append(kwargs[kw])
            colors.append(kw)
        return self.encode(
            color=Color(column, scale=Scale(domain=levels, range=colors))
        )

    def qcolormap(self, column: str, **kwargs) -> "Chart":
        """Add a quantiles based colormap to the chart

        :param column: the column to use
        :type column: str
        :param kwargs: the colors and values map to use
        :type kwargs: Dict[str,str]
        :raises ArgumentError: raised if less than two colors are provided
        :return: the chart object
        :rtype: Chart
        """
        if len(kwargs) < 2:
            raise ArgumentError("Provide at least two colors in the map")
        levels: List = []
        colors: List[str] = []
        for kw in kwargs.keys():
            q = self.data[column].quantile(kwargs[kw])
            levels.append(q)
            colors.append(kw)
        # levels.append(self.data[column].max())
        return self.encode(
            color=Color(column, scale=Scale(domain=levels, range=colors))
        )


class AltairChart:
    x: Optional[X] = None
    y: Optional[Y] = None
    default_width: int
    default_height: int = 0

    def __init__(self, default_width: int) -> None:
        self.default_width = default_width
        """if is_notebook is True:
            try:
                renderers.enable("notebook")
            except Exception:
                pass"""

    def chart(
        self,
        df: pd.DataFrame,
        chart_type: str,
        x: Optional[Union[str, X]] = None,
        y: Optional[Union[str, X]] = None,
        **kwargs
    ) -> Chart:
        """
        Get an Altair chart object
        """
        if x is not None and y is not None:
            self.set_axis(x, y)
        self._checkAxis()
        opts = {}
        style = {}
        encode = {}
        k = kwargs.keys()
        if "opts" in k:
            opts = kwargs["opts"]
        if "style" in k:
            style = kwargs["style"]
        if "encode" in k:
            encode = kwargs["encode"]

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
        elif chart_type == "hist":
            chart = self._altair_histogram(df, opts, style, encode)
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
        assert self.x is not None and self.y is not None, "Set the chart fields"
        if chart_type == "line":
            c = Chart(df).mark_line(**style).encode(x=self.x, y=self.y, **encode)
        elif chart_type == "bar":
            c = Chart(df).mark_bar(**style).encode(x=self.x, y=self.y, **encode)
        elif chart_type == "point":
            c = Chart(df).mark_point(**style).encode(x=self.x, y=self.y, **encode)
        else:
            raise Exception("Unknown chart type")
        # encoder = encode
        # if "text" not in encoder:
        #    encoder["text"] = self.y
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
        num = c.mark_text(**style).encode(text=self.y.shorthand)
        res = (c + num).properties(**opts)
        return res

    def _altair_hline_(self, df: pd.DataFrame, opts, style, encode) -> Chart:
        """
        Get a mean line chart
        """
        assert self.x is not None and self.y is not None, "Set the chart fields"
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
            # hx = X(self.x.title, axis=None)
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

    def _altair_histogram(self, df: pd.DataFrame, opts, style, encode) -> Chart:
        assert self.x is not None and self.y is not None, "Set the chart fields"
        return (
            Chart(df)
            .mark_bar(**style)
            .encode(X(self.x.shorthand, bin=True), y="count()", **encode)
            .properties(**opts)
        )

    def set_axis(self, xaxis: Union[str, X], yaxis: Union[str, Y]) -> None:
        if isinstance(xaxis, X):
            self.x = xaxis
        else:
            self.x = X(xaxis, scale=Scale(zero=False))
        if isinstance(yaxis, Y):
            self.y = yaxis
        else:
            self.y = Y(yaxis, scale=Scale(zero=False))

    def _checkAxis(self) -> None:
        assert self.x is not None and self.y is not None, "Set the chart fields"

    def _default_opts(self, opts: Dict) -> Dict:
        if "width" not in opts:
            opts["width"] = self.default_width
        if "height" not in opts:
            if self.default_height > 0:
                opts["height"] = self.default_height
        return opts
