import os
import uuid
from typing import List, Optional

try:
    from fpdf import FPDF
except (ModuleNotFoundError, ImportError):
    print("The pdf reporting engine is not available in this environment")


from dataspace.types import ReportItemType, ChartType
from dataspace.utils.messages import msg_info, msg_ok


class ReportEngine:
    """
    Class to handle reporting
    """

    path: str = ""
    items: List[ReportItemType] = []

    def stack(
        self,
        chart: ChartType,
        title: Optional[str] = None,
        description: Optional[str] = None,
    ):
        """
        Store a chart in the report stack
        """
        self.items.append(ReportItemType(chart, title, description))

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
                pdf.cell(txt=item.description + "\n")
            path = self.path + "/" + uuid.uuid4().hex + ".png"
            item.chart.save_img(path)
            imgs.append(path)
            pdf.image(path, w=pdf.epw)
        pdf.output(self.path + "/" + filename)
        if clear_stack is True:
            self.items = []
        # cleanup
        for img in imgs:
            os.remove(img)

    def write_file(self, filename: str, folderpath: str, html: str) -> str:
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
