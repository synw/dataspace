from dataspace.core import DataSpace
from dataspace.core.env import is_notebook
from dataspace.core.load import from_df, from_csv, from_django

__all__ = [
    "DataSpace",
    "is_notebook",
    "from_df",
    "from_csv",
    "from_django",
]
