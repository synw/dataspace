from typing import Literal, Optional, Union
from dataclasses import dataclass
from dataspace.charts.altair import AltairChart

from dataspace.charts.bokeh.bokeh import BokehChart


ChartEngineType = Literal["altair", "bokeh"]

ChartType = Union[AltairChart, BokehChart]


@dataclass
class ReportItemType:
    chart: ChartType
    title: Optional[str]
