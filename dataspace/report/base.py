import os
from typing import List, Optional
from dataspace.types import ReportItemType, ChartType

from dataspace.utils.messages import msg_info, msg_ok
# from dataspace.core.env import is_notebook


class Report():
    """
    Class to handle reporting
    """
    path: str
    items: List[ReportItemType] = []

    def __init__(self, path: str):
        """
        Initialize
        """
        self.path = path

    def stack(self, chart: ChartType, title: Optional[str]):
        """
        Store a chart in the report stack
        """
        self.items.append(ReportItemType(chart, title))

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