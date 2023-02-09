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
        """Set the width of the chart

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.line_().w(500)

        :param v: value in pixels
        :type v: int
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(width=v)

    def h(self, v: int) -> "AltairChart":
        """Set the height of the chart

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.line_().h(200)

        :param v: value in pixels
        :type v: int
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(height=v)

    def wh(self, w: int, h: int) -> "AltairChart":
        """Set the width and height of a chart

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.line_().wh(500, 200)

        :param w: width value in pixels
        :type w: int
        :param h: height value in pixels
        :type h: int
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(width=w, height=h)

    def mw(self, v: int) -> "AltairChart":
        """Configure the default mark width

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.bar_().mw(7)

        :param v: width value in pixels
        :type v: int
        :return: the chart object
        :rtype: Chart
        """
        return self.configure_mark(width=v)

    def pw(self, v: int) -> "AltairChart":
        """Configure the default point width

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.point_().pw(25)

        :param v: width value in pixels
        :type v: int
        :return: the chart object
        :rtype: Chart
        """
        return self.configure_point(size=v)

    def color(self, v: str) -> "AltairChart":
        """Configure the chart color

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.area_().color("forestgreen")

        :param v: the color value
        :type v: str
        :return: the chart object
        :rtype: Chart
        """
        return self.encode(color=value(v))

    def opacity(self, v: Union[int, float]) -> "AltairChart":
        """Configure the chart opacity

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.axis("date:T", "price:Q")
            ds.point_().opacity(0.5)

        :param v: the opacity value
        :type v: Union[int, float]
        :return: the chart object
        :rtype: Chart
        """
        return self.encode(opacity=value(v))

    def tooltip(self, v: Union[str, List[str]]) -> "AltairChart":
        """Configure a tooltip on hover for some colums

        The tooltip shows up when the user cursor goes
        over the datapoint on the chart

        .. code-block:: python

            ds = await load_dataset("sp500")
            ds.point_("date:T", "price:Q").tooltip(["date","price"])

        :param v: column or list of columns to use for the tooltip
        :type v: Union[str, List[str]]
        :return: the chart object
        :rtype: Chart
        """
        return self.encode(tooltip=v)

    def to(self, v: str) -> "AltairChart":
        """Change the chart type for an existing chart (only for the Altair engine)

        :param v: the new chart type
        :type v: str
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(mark=v)

    def rx(self, v=-45) -> "AltairChart":
        """Rotate the chart x labels

        :param v: angle of rotation to use, defaults to -45
        :type v: int, optional
        :return: the chart object
        :rtype: Chart
        """
        self.encoding.x.axis.labelAngle = v
        return self

    def nox(self) -> "AltairChart":
        """Remove the x axis labels

        .. code-block:: python

            ds = await load_dataset("timeserie")
            ds.axis("date:T", "data:Q")
            (ds.line_().nox() + ds.point_().nox())

        :return: the chart object
        :rtype: Chart
        """
        self.encoding.x.axis = None
        return self

    def noy(self) -> "AltairChart":
        """Remove the y axis labels

        .. code-block:: python

            ds = await load_dataset("timeserie")
            ds.axis("date:T", "data:Q")
            (ds.line_().noy() + ds.point_().noy())

        :return: the chart object
        :rtype: Chart
        """
        self.encoding.y.axis = None
        return self

    def title(self, v: str) -> "AltairChart":
        """Add a text title to the chart

        .. code-block:: python

            ds = await load_dataset("timeserie")
            ds.area_("date:T", "data:Q").title("The chart title")


        :param v: the title text
        :type v: str
        :return: the chart object
        :rtype: Chart
        """
        return self.properties(title=v)

    def colormap(self, column: str, **kwargs) -> "AltairChart":
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

    def qcolormap(self, column: str, **kwargs) -> "AltairChart":
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

    def save_img(self, path: str):
        """Save the chart to a png image

        :param path: the filepath
        :type path: str
        """
        save(self, path)

    def get_html_(self) -> str:
        """
        Get html for an Altair chart
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
        Returns html script tags for Altair
        """
        header = (
            f'<script src="https://cdn.jsdelivr.net/npm/vega@{VEGA_VERSION}"></script>',
            f'<script src="https://cdn.jsdelivr.net/npm/vega-lite@{VEGALITE_VERSION}"></script>',
            f'<script src="https://cdn.jsdelivr.net/npm/vega-embed@{VEGAEMBED_VERSION}"></script>',
            "<style>.vega-actions {display:none}</style>",
        )
        return "\n".join(header)
