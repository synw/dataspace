import os
import uuid
from typing import List, Optional

try:
    from slugify import slugify
except (ModuleNotFoundError, ImportError):
    # print("The html reporting engine is not available in this environment")
    pass

try:
    from fpdf import FPDF
except (ModuleNotFoundError, ImportError):
    # print("The pdf reporting engine is not available in this environment")
    pass


from dataspace.types import ChartEngineName, ReportItemType, ChartType
from dataspace.utils.messages import msg_end, msg_info, msg_ok, msg_start
from dataspace.charts.altair.charts import AltairChart
from dataspace.charts.bokeh.charts import HvChart


class ReportEngine:
    """
    Class to handle reporting
    """

    path: str = ""
    items: List[ReportItemType] = []
    has_altair_chart = False
    has_bokeh_chart = False

    def stack(
        self,
        chart: ChartType,
        chart_engine: ChartEngineName,
        title: Optional[str] = None,
        description: Optional[str] = None,
    ):
        """
        Store a chart in the report stack
        """
        id = uuid.uuid4().hex
        if title is not None:
            id = slugify(title)
        self.items.append(ReportItemType(id, chart, chart_engine, title, description))
        if chart_engine == "altair":
            self.has_altair_chart = True
        elif chart_engine == "bokeh":
            self.has_bokeh_chart = True

    def save_pdf(self, filename: str, clear_stack=True):
        """
        Save a report to a pdf file
        """
        if self.path == "":
            raise ValueError("Please set a report path first")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", size=12)
        imgs = []
        for item in self.items:
            if item.title:
                pdf.write(txt=item.title + "\n")
            if item.description:
                pdf.write(txt=item.description + "\n")
            path = self.path + "/" + item.id + ".png"
            item.chart.save_img(path)
            imgs.append(path)
            pdf.image(path, w=pdf.epw)
        pdf.output(self.path + "/" + filename)
        if clear_stack is True:
            self._clear_stack()
        # cleanup
        for img in imgs:
            os.remove(img)

    def save_html(self, info=False, clear_stack=True):
        """
        Save a report to html files
        """
        if self.path == "":
            raise ValueError("Please set a report path first")
        msg_start("Exporting report to html files")
        for item in self.items:
            self.write_html_file(item.id, self.path, item.chart.get_html_())
        if info is True:
            if self.has_altair_chart is True:
                msg_info(f"Altair html headers:\n{AltairChart.html_header_()}")
            if self.has_bokeh_chart is True:
                msg_info(f"Bokeh html headers:\n{HvChart.html_header_()}")
        msg_end("Report exported to html files")
        if clear_stack is True:
            self._clear_stack()

    def write_html_file(self, filename: str, folderpath: str, html: str) -> str:
        """
        Writes some html to a file
        """

        # check directories
        if not os.path.isdir(folderpath):
            os.makedirs(folderpath)
            msg_info("Creating directory " + folderpath)
        # construct file path
        filepath = folderpath + "/" + filename + ".html"
        # write the file
        filex = open(filepath, "w")
        filex.write(html)
        filex.close()
        msg_ok("File written to", filepath)
        return filepath

    def _clear_stack(self):
        """
        Clear the reporting stack
        """
        self.items = []
        self.has_altair_chart = False
        self.has_bokeh_chart = False
