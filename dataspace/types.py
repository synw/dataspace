from typing import Literal, Optional, Union
from dataclasses import dataclass
from dataspace.charts.altair import AltairChart

from dataspace.charts.bokeh import HvChart


ChartEngineName = Literal["altair", "bokeh"]

ChartType = Union[AltairChart, HvChart]


@dataclass
class ReportItemType:
    chart: ChartType
    title: Optional[str]
    description: Optional[str]
