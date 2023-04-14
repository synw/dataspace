from ctypes import ArgumentError
from typing import List, Union
import uuid

from altair import Chart as AltChart
from altair import (
    Color,
    Scale,
    value,
    VEGA_VERSION,
    VEGALITE_VERSION,
    VEGAEMBED_VERSION,
)

try:
    from altair_saver import save
except (ModuleNotFoundError, ImportError):
    print("The Altair chart saver is not available in this environment")


class AltairChart(AltChart):
    def w(self, v: int) -> "AltairChart":
        """
        Set the width of the chart.

        Args:
            v (int): Value in pixels.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to set the width of a chart to 500 pixels:
            chart = ds.line_()
            chart.w(500)
        """
        return self.properties(width=v)

    def h(self, v: int) -> "AltairChart":
        """
        Set the height of the chart.

        Args:
            v (int): Value in pixels.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to set the height of a chart to 200 pixels:
            chart = ds.line_()
            chart.h(200)
        """
        return self.properties(height=v)

    def wh(self, w: int, h: int) -> "AltairChart":
        """
        Set the width and height of a chart.

        Args:
            w (int): Width value in pixels.
            h (int): Height value in pixels.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to set the width and height of a chart:
            chart = ds.line_()
            chart.wh(500, 200)
        """
        return self.properties(width=w, height=h)

    def mw(self, v: int) -> "AltairChart":
        """
        Configure the default mark width.

        Args:
            v (int): Width value in pixels.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to configure the default mark width:
            chart = ds.bar_()
            chart.mw(7)
        """
        return self.configure_mark(width=v)

    def pw(self, v: int) -> "AltairChart":
        """
        Configure the default point width.

        Args:
            v (int): Width value in pixels.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to configure the default point width:
            chart = ds.point_()
            chart.pw(25)
        """
        return self.configure_point(size=v)

    def color(self, v: str) -> "AltairChart":
        """
        Configure the chart color.

        Args:
            v (str): The color value.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to configure the chart color:
            chart = ds.area_()
            chart.color("forestgreen")
        """
        return self.encode(color=value(v))

    def opacity(self, v: Union[int, float]) -> "AltairChart":
        """
        Configure the chart opacity.

        Args:
            v (Union[int, float]): The opacity value.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to configure the chart opacity:
            chart = ds.point_()
            chart.opacity(0.5)
        """
        return self.encode(opacity=value(v))

    def tooltip(self, v: Union[str, List[str]]) -> "AltairChart":
        """
        Configure a tooltip on hover for some columns.

        The tooltip shows up when the user cursor goes
        over the datapoint on the chart.

        Args:
            v (Union[str, List[str]]): Column or list of columns to use for the tooltip.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to configure a tooltip for some columns:
            chart = ds.point_()
            chart.tooltip(["date", "price"])
        """
        return self.encode(tooltip=v)

    def to(self, v: str) -> "AltairChart":
        """
        Change the chart type for an existing chart (only for the Altair engine).

        Args:
            v (str): The new chart type.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to change the chart type:
            chart = ds.line_()
            chart.to("area")
        """
        return self.properties(mark=v)

    def rx(self, v=-45) -> "AltairChart":
        """
        Rotate the chart x labels.

        Args:
            v (int, optional): Angle of rotation to use. Defaults to -45.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to rotate the x labels:
            chart = ds.line_()
            chart = chart.rx(-45)
        """
        self.encoding.x.axis.labelAngle = v
        return self

    def nox(self) -> "AltairChart":
        """
        Remove the x-axis labels.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to remove the x-axis labels:
            ds.line_().nox() + ds.point_().nox()
        """
        self.encoding.x.axis = None
        return self

    def noy(self) -> "AltairChart":
        """
        Remove the y-axis labels.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to remove the y-axis labels:
            ds.line_().noy() + ds.point_().noy()
        """
        self.encoding.y.axis = None
        return self

    def title(self, v: str) -> "AltairChart":
        """
        Add a text title to the chart.

        Args:
            v (str): The title text.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to add a title to the chart:
            ds.area_("date:T", "data:Q").title("The chart title")
        """
        return self.properties(title=v)

    def colormap(self, column: str, **kwargs) -> "AltairChart":
        """
        Add a values-based colormap to the chart.

        Args:
            column (str): The column to use for the colormap.
            **kwargs: The colors and values map to use.

        Raises:
            ArgumentError: Raised if less than two colors are provided.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to add a colormap to the chart:
            ds.point_().colormap("Origin", Japan="red", Europe="green", USA="blue")
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

    def qcolormap(self, column: str, **kwargs) -> "AltairChart":
        """
        Add a quantiles-based colormap to the chart.

        Args:
            column (str): The column to use for the colormap.
            **kwargs: The quantile values and colors map to use.

        Raises:
            ArgumentError: Raised if less than two colors are provided.

        Returns:
            AltairChart: The chart object.

        Example:
            # Use this method to add a quantiles-based colormap to the chart:
            ds.axis("Horsepower:Q", "Miles_per_Gallon:Q")
            chart = ds.point_().qcolormap("Origin", low=0.2, high=0.8, Japan="red", Europe="green", USA="blue")

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

    def save_img(self, path: str):
        """
        Save the chart to a png image.

        Args:
            path (str): The filepath.
        """
        save(self, path)

    def get_html_(self) -> str:
        """
        Get HTML for an Altair chart.

        Returns:
            str: The HTML string representing the chart.
        """
        slug = uuid.uuid4().hex
        json_data = self.to_json(indent=0)
        html = '<div id="' + slug + '"></div>\n'
        html += '<script type="text/javascript">'
        html += "var spec = " + json_data.replace("\n", "") + ";"
        html += """
        var embed_opt = {"mode": "vega-lite"};
        function showError(altel, error){
            altel.innerHTML = ('<div class="error">'
                            + '<p>JavaScript Error: ' + error.message + '</p>'
                            + "<p>This usually means there's a typo in your "
                            + "chart specification. "
                            + "See the javascript console for the full "
                            + "traceback.</p>"
                            + '</div>');
            throw error;
        };\n"""
        html += "const el_" + slug + " = document.getElementById('" + slug + "');"
        html += "vegaEmbed('#" + slug + "', spec, embed_opt)"
        html += ".catch(error => showError(el_" + slug + ", error));"
        html += "</script>"
        return html

    @staticmethod
    def html_header_():
        """
        Returns the HTML script tags

        Returns:
            str: The HTML script tags
        """
        header = (
            f'<script src="https://cdn.jsdelivr.net/npm/vega@{VEGA_VERSION}"></script>',
            f'<script src="https://cdn.jsdelivr.net/npm/vega-lite@{VEGALITE_VERSION}"></script>',
            f'<script src="https://cdn.jsdelivr.net/npm/vega-embed@{VEGAEMBED_VERSION}"></script>',
            "<style>.vega-actions {display:none}</style>",
        )
        return "\n".join(header)
