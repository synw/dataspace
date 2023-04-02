from typing import Any, Dict, List, Optional

import pandas as pd
import polars as pl

from dataspace.calculations import _percent, _diffm, _diffp, _cvar, _lreg
from dataspace.charts import DsChartEngine
from dataspace.clean import (
    _drop_any_nulls,
    _drop_all_nulls,
    _fdate,
    _fill_nulls,
    _replace,
    _roundvals,
    _strip,
    _strip_cols,
    _timestamps,
    _to_date,
    _to_tzdate,
    _to_float,
    _to_int,
    _to_str,
    _to_type,
)
from dataspace.core.env import is_notebook
from dataspace.count import _count_empty_, _count_null_, _count_unique_, _count_zero_

# from dataspace.info import _cols
from dataspace.info.view import _show
from dataspace.io.export import export_csv
from dataspace.transform import _drop, _rename, _add, _resample
from dataspace.types import ChartType
from dataspace.utils.messages import msg_info, msg_ok
from dataspace.report import ReportEngine


class DataSpace:
    df: pl.DataFrame
    _charts: DsChartEngine = DsChartEngine()
    _reports: ReportEngine = ReportEngine()

    def __init__(self, df: pl.DataFrame | pl.LazyFrame):
        if isinstance(df, pl.LazyFrame):
            self.df = df.collect()
        else:
            self.df = df

    def __repr__(self) -> str:
        num = self.df.height
        msg = f"<DataSpace object | {num} rows>"
        if is_notebook is True:
            self.show()
        return msg

    # **************************
    #           info
    # **************************

    def show(self, rows: int = 5) -> pl.DataFrame:
        """
        Displays information about the DataFrame.

        Args:
            rows (int, optional): The number of rows to show. Defaults to 5.

        Returns:
            pl.DataFrame: A head of the DataFrame.

        Example:
            ds.show()
        """
        return _show(rows, self.df)

    """def cols_(self) -> pd.DataFrame:
        
        Returns a dataframe with columns info

        Category: Info/View data/Show

        :return: a pandas dataframe
        :rtype: ``DataFrame``

        :example: `ds.cols_()`
        
        return _cols(self.df)"""

    # **************************
    #           clean
    # **************************

    def to_date(self, *cols: str, fmt: str = "%Y-%m-%d %H:%M:%S"):
        """
        Converts some column values to date type.

        Args:
            cols (str): The name(s) of the column(s) to convert.
            fmt (str): The date parsing format to use

        Example:
            ds.to_date("mycol")
        """
        self.df = _to_date(self.df, *cols, fmt=fmt)

    def to_tzdate(self, *cols: str):
        """
        Converts some column values to date type from ISO string
        with timezone info.

        Args:
            cols (str): The name(s) of the column(s) to convert.

        Example:
            ds.to_date("mycol")
        """
        self.df = _to_tzdate(self.df, *cols)

    def to_int(self, *cols: str):
        """
        Converts some column values to integers.

        Args:
            *cols (str): The name(s) of the column(s) to convert.

        Example:
            ds.to_int("mycol1", "mycol2")
        """
        self.df = _to_int(self.df, *cols)
        if is_notebook is True:
            msg_ok("Converted columns values to integers")

    def to_float(self, *cols: str):
        """
        Converts column values to floats.

        Args:
            cols (str): The name(s) of the column(s) to convert.

        Example:
            ds.to_float("mycol1")
        """
        self.df = _to_float(self.df, *cols)
        if is_notebook is True:
            msg_ok("Converted columns values to floats")

    def to_str(self, *cols: str):
        """
        Converts column values to strings.

        Args:
            cols (str): The name(s) of the column(s) to convert.

        Example:
            ds.to_str("mycol1")
        """
        self.df = _to_str(self.df, *cols)
        if is_notebook is True:
            msg_ok("Converted columns values to strings")

    def to_type(self, dtype: pl.DataType, *cols: str):
        """
        Converts column values to a given Polars datatype in the main DataFrame.

        Args:
            dtype (pl.DataType): The data type to convert to.
            *cols (str): The name(s) of the column(s) to convert.

        Example:
            ds.to_type(pl.Utf8, "mycol")
        """
        self.df = _to_type(self.df, dtype, *cols)
        if is_notebook is True:
            msg_ok(f"Converted columns values to {dtype}")

    def drop_any_nulls(self, *cols: str):
        """
        Drop rows that contain any null values in the
        specified columns.

        Args:
            *cols: A variable number of string arguments representing the column
                names to check for null values.

        Example:
            ds.drop_any_nulls("mycol")
        """
        self.df = _drop_any_nulls(self.df, *cols)

    def drop_all_nulls(self):
        """
        Drop rows where all values are null

        Args:
            *cols: A variable number of string arguments representing the column
                names to check for null values.

        Example:
            ds.drop_all_nulls()
        """
        self.df = _drop_all_nulls(self.df)

    def fill_nulls(self, *cols: str, val: Any, nulls=[None]):
        """
        Replace null (missing or empty) values in the specified columns with a given value.

        Args:
            *cols (str): One or more column names to replace nulls in.
            val (any, optional): The value to replace nulls with. Defaults to None.
            nulls (list, optional): The list of null values to replace. Defaults to [None].

        Returns:
            None

        Raises:
            ValueError: If any of the specified column names are not found in the
                DataFrame.

        Example:
            ds.fill_nulls("mycol")
        """
        self.df = _fill_nulls(self.df, *cols, val=val, nulls=nulls)

    def fdate(self, *cols, precision: str = "S", newcol="fdate"):
        """
        Converts specified columns to formatted date strings.

         Args:
             cols (str): Names of columns to convert to formatted date strings.
             precision (str, optional): Precision level of date format string.
                 Defaults to "S" (seconds).
                 Possible values: "S" (seconds), "Min" (minutes), "H" (hours), "D" (days),
                 "M" (months), "Y" (years).
             newcol: Name of the new column to create. Defaults to "fdate".

         Example:
             ds.fdate("mycol1", "mycol2")
        """
        self.df = _fdate(self.df, *cols, precision=precision, newcol=newcol)

    def timestamps(self, *cols: str, name: str = "timestamps"):
        """
        Adds a new column with timestamps from one or more specified date columns.

        Args:
            *cols (str): Names of columns to convert to timestamps.
            name (str, optional): Name of the new column to create. Defaults to "timestamps".


        Example:
            ds.timestamps("mycol")
        """
        self.df = _timestamps(self.df, *cols, name=name)

    def strip(self, *cols: str):
        """
        Removes leading and trailing white spaces from the
        values in the specified columns.

        Args:
            *cols (str): Names of columns to strip

        Example:
            ds.strip("mycol")
        """
        self.df = _strip(self.df, *cols)

    def strip_cols(self):
        """
        Remove leading and trailing white spaces in columns names

        Example:
            ds.strip_cols()
        """
        self.df = _strip_cols(self.df)

    def roundvals(self, col: str, precision: int = 2):
        """
        Rounds the values in the specified column to the specified float precision.

        Args:
            col (str): Name of the column to round.
            precision (int, optional): Number of decimal places to round to. Defaults to 2.

        Example:
            ds.roundvals("mycol")
        """
        self.df = _roundvals(self.df, col, precision)

    def replace(self, col: str, searchval: Any, replaceval: Any):
        """
        Replaces all occurrences of a value in the specified column with a new value.

        Args:
            col (str): Name of the column to search.
            searchval (str): Value to replace.
            replaceval (str): New value to replace `searchval` with.

        Example:
            ds.replace("mycol", "value", "new_value")
        """
        self.df = _replace(self.df, col, searchval, replaceval)

    # **************************
    #           select
    # **************************

    def limit(self, r: int = 5):
        """
        Limits the number of rows in the DataFrame to the specified number.

        Args:
            r (int, optional): Number of rows to keep. Defaults to 5.

        Example:
            ds.limit(100)
        """
        self.df = self.df.limit(r)

    def unique_(self, col: str) -> List[str]:
        """
        Returns a list of unique values in the specified column.

        Args:
            col (str): Name of the column to select from.

        Returns:
            list: A list of unique values in the column.

        Example:
            ds.unique_("col1")
        """
        l = list(self.df[col].unique())
        l.sort()
        return l

    def wunique_(self, col: str, colname: str = "Number") -> pd.DataFrame:
        """
        Returns a `pl.DataFrame` object with a count of unique values in the specified column.

        Args:
            col (str): Name of the column to select from.
            colname (str, optional): Name of the new column containing the unique counts.
                Defaults to "Number".

        Example:
            ds.wunique_("col1")
        """
        return self.df.groupby(col).agg([pl.col(col).count().alias(colname)])

    # **************************
    #           count
    # **************************

    def count_null_(self, col: str) -> int:
        """
        Counts the number of null values in the specified column.

        Args:
            col (str): Name of the column to count from.

        Returns:
            int: The number of null values in the column.

        Example:
            ds.count_nulls_("col1")
        """
        return _count_null_(self.df, col)

    def count_empty_(self, col: str) -> int:
        """
        Counts the number of empty values in the specified column.

        Args:
            col (str): Name of the column to count from.

        Returns:
            int: The number of empty values in the column.

        Example:
            ds.count_empty_("col1")
        """
        return _count_empty_(self.df, col)

    def count_zero_(self, col: str) -> int:
        """
        Counts the number of zero values in the specified column.

        Args:
            col (str): Name of the column to count from.

        Returns:
            int: The number of zero values in the column.

        Example:
            ds.count_zero_("col1")
        """
        return _count_zero_(self.df, col)

    def count_unique_(self, col: str) -> int:
        """
        Counts the number of unique values in the specified column.

        Args:
            col (str): Name of the column to count from.

        Returns:
            int: The number of unique values in the column.

        Example:
           ds.count_unique_("col1")
        """
        return _count_unique_(self.df, col)

    # **************************
    #        transform
    # **************************

    def split_(self, col: str) -> Dict[str, "DataSpace"]:
        """
        Splits the main `pl.DataFrame` object into multiple `DataSpace` objects,
        one for each unique value in the specified column.

        Args:
            col (str): Name of the column to split by.

        Returns:
            Dict[str, DataSpace]: A dictionary with the unique values in the specified column as
                keys and a corresponding `DataSpace` object as the value.

        Example:
            dss = ds.split_("col1")
        """
        dss = {}
        unique = self.df[col].unique().to_list()
        for key in unique:
            dss[key] = DataSpace(self.df.filter(pl.col(col) == key))
        return dss

    def sort(self, col: str):
        """
        Sorts the main `pl.DataFrame` object in-place according to the specified column.

        Args:
            col (str): Name of the column to sort by.

        Example:
            ds.sort("Col 1")
        """
        self.df = self.df.sort(by=col)

    def drop(self, *cols):
        """
        Removes the specified columns from the main `pl.DataFrame` object in-place.

        Args:
            *cols (str): Names of the columns to remove.

        Example:
            ds.drop("Col1", "Col2")
        """
        self.df = _drop(self.df, *cols)

    def rename(self, source_col: str, dest_col: str):
        """
        Renames a column in the main `pl.DataFrame` object in-place.

        Args:
            source_col (str): Name of the column to rename.
            dest_col (str): New name of the column.

        Example:
            ds.rename("Col1", "Newcol")
        """
        self.df = _rename(self.df, source_col, dest_col)

    def add(self, col: str, value: Any):
        """
        Adds a new column to the main `pl.DataFrame` object with the
        specified default value.

        Args:
            col (str): Name of the new column.
            value (Any): Default value for the new column.

        Example:
            ds.add("Col 4", 0)
        """
        self.df = _add(self.df, col, value)

    def keep(self, *cols: str):
        """
        Limits the main `pl.DataFrame` object to the specified columns.

        Args:
            *cols (str): Names of the columns to keep.

        Example:
            ds.keep("Col 1", "Col 2")
        """
        self.df = self.df.select(cols)

    def exclude(self, col: str, val: Any):
        """
        Deletes all rows from the main `pl.DataFrame` object
        where the specified column has the specified value.

        Args:
            col (str): Name of the column to check for the specified value.
            val (Any): Value to exclude rows for.

        Example:
            ds.exclude("Col1", "value")
        """
        self.df = self.df.filter(pl.any(pl.col(col) != val))

    def copycol(self, origin_col: str, dest_col: str):
        """
        Copies the values from one column to another column
        in the main `pl.DataFrame` object.

        Args:
            origin_col (str): Name of the column to copy values from.
            dest_col (str): Name of the column to copy values to.

        Example:
            ds.copy("col1", "New col")
        """
        self.df = self.df.with_columns([pl.col(origin_col).alias(dest_col)])

    def reverse(self):
        """
        Reverses the main dataframe order

        Example:
            ds.reverse()
        """
        self.df = self.df.reverse()

    def resample(
        self,
        date_col: str,
        time_period: str,
        mcols: List[str] = [],
        scols: List[str] = [],
    ):
        """
        Resamples the `pl.DataFrame` object to a specific time period.

        Args:
            date_col (str): Name of the column containing the date or datetime values.
            time_period (str): Resample time period string. Possible values are:
                - "1ns" (1 nanosecond)
                - "1us" (1 microsecond)
                - "1ms" (1 millisecond)
                - "1s" (1 second)
                - "1m" (1 minute)
                - "1h" (1 hour)
                - "1d" (1 day)
                - "1w" (1 week)
                - "1mo" (1 calendar month)
                - "1y" (1 calendar year)
                - "1i" (1 index count)
            mcols (List[str]): List of column names to resample with the mean function.
            scols (List[str]): List of column names to resample with the sum function.

        Example:
            ds.resample("datecol", "1m", mean_cols=["price"], sum_cols=["quantity"])
        """
        self.df = _resample(self.df, date_col, time_period, mcols, scols)

    def rsum(self, date_col: str, time_period: str, *cols: str):
        """
        Resamples the `pl.DataFrame` object and sum to a specific time period.

        Args:
            date_col (str): Name of the column containing the date or datetime values.
            time_period (str): Resample time period string. Possible values are:
                - "1ns" (1 nanosecond)
                - "1us" (1 microsecond)
                - "1ms" (1 millisecond)
                - "1s" (1 second)
                - "1m" (1 minute)
                - "1h" (1 hour)
                - "1d" (1 day)
                - "1w" (1 week)
                - "1mo" (1 calendar month)
                - "1y" (1 calendar year)
                - "1i" (1 index count)
            *cols (str): column names to resample with the sum function.

        Example:
            ds.rsum("datecol", "1m", "quantity")
        """
        self.resample(date_col, time_period, scols=list(cols))

    def rmean(self, date_col: str, time_period: str, *cols: str):
        """
        Resamples the `pl.DataFrame` object and mean to a specific time period.

        Args:
            date_col (str): Name of the column containing the date or datetime values.
            time_period (str): Resample time period string. Possible values are:
                - "1ns" (1 nanosecond)
                - "1us" (1 microsecond)
                - "1ms" (1 millisecond)
                - "1s" (1 second)
                - "1m" (1 minute)
                - "1h" (1 hour)
                - "1d" (1 day)
                - "1w" (1 week)
                - "1mo" (1 calendar month)
                - "1y" (1 calendar year)
                - "1i" (1 index count)
            *cols (str): column names to resample with the mean function.

        Example:
            ds.rmean("datecol", "1m", "price")
        """
        self.resample(date_col, time_period, mcols=list(cols))

    # **************************
    #        calculations
    # **************************

    def percent(self, col: str, roundn=1):
        """Adds a percent column to the DataFrame.

        Args:
            col (str): The name of the column to calculate percentages from.
            roundn (int, optional): The number of decimal places to round to. Defaults to 1.

        Returns:
            polars.DataFrame: The DataFrame with a new column containing the percentages.

        Example:
            ds.percent("amount")
        """
        self.df = _percent(self.df, col, roundn)

    def diffp(self, diffcol: str, name: str = "diff", decimals=0):
        """
        Add a diff column to the main dataframe: calculate the difference
        from the previous value.

        Args:
            diffcol (str): The column name for which to calculate the difference.
            name (str, optional): The name of the resulting difference column. Defaults to "diff".
            decimals (int, optional): The number of decimal places to round the difference to. Defaults to 0.

        Example:
            ds.diffp("Col 1", "New col")
        """
        self.df = _diffp(
            self.df, diffcol=diffcol, name=name, decimals=decimals, percent=False
        )

    def diffpp(self, diffcol: str, name: str = "diff", decimals=0):
        """
        Add a diff column to the main dataframe: calculate the difference
        in percentage from the previous value.

        Args:
            diffcol (str): The column name for which to calculate the difference.
            name (str, optional): The name of the resulting difference column. Defaults to "diff".
            decimals (int, optional): The number of decimal places to round the difference to. Defaults to 0.

        Example:
            ds.diffpp("Col 1", "New col")
        """
        self.df = _diffp(
            self.df, diffcol=diffcol, name=name, decimals=decimals, percent=True
        )

    def diffm(self, diffcol: str, name: str = "diff", decimals=0):
        """
        Add a difference column to the main dataframe: calculate the
        difference from the column mean.

        Args:
            diffcol (str): The column name for which to calculate the difference.
            name (str, optional): The name of the resulting difference column. Defaults to "diff".
            decimals (int, optional): The number of decimal places to round the difference to. Defaults to 0.

        Example:
            ds.diffm("Col 1", "New col")
        """
        self.df = _diffm(self.df, diffcol, name=name, decimals=decimals, percent=False)

    def diffmp(self, diffcol: str, name: str = "diff", decimals=0):
        """
        Add a difference column to the main dataframe: calculate the
        difference in percentage from the column mean.

        Args:
            diffcol (str): The column name for which to calculate the difference.
            name (str, optional): The name of the resulting difference column. Defaults to "diff".
            decimals (int, optional): The number of decimal places to round the difference to. Defaults to 0.

        Example:
            ds.diffmp("Col 1", "New col")
        """
        self.df = _diffm(self.df, diffcol, name=name, decimals=decimals, percent=True)

    def cvar_(self, col: str) -> float:
        """
        Returns the coefficient of variation (CV) of a column in percentage.

        Args:
            col (str): The name of the column for which to calculate the coefficient of variation.

        Returns:
            float: The coefficient of variation of the column in percentage.

        Example:
            ds.cvar_("mycol")
        """
        return _cvar(self.df, col)

    def lreg_(self, xcol: str, ycol, name="regression"):
        self.df = _lreg(self.df, xcol, ycol, name)

    """
    def diffs(self, col: str, serie: Iterable, name: str = "Diff"):
        ""
        Add a diff column from a serie. The serie is an iterable
        of the same length than the dataframe

        :param col: column to diff
        :type col: str
        :param serie: serie to diff from
        :type serie: iterable
        :param name: name of the diff col, defaults to "Diff"
        :param name: str, optional

        :example: ``ds.diffs("Col 1", [1, 1, 4], "New col")``
        ""
        self.df = _diffs(self.df, col, serie, name)

    def diffsp(self, col: str, serie: Iterable, name: str = "Diff"):
        ""
        Add a diff column in percentage from a serie. The serie is
        an iterable of the same length than the dataframe

        :param col: column to diff
        :type col: str
        :param serie: serie to diff from
        :type serie: iterable
        :param name: name of the diff col, defaults to "Diff"
        :param name: str, optional

        :example: ``ds.diffp("Col 1", [1, 1, 4], "New col")``
        ""
        self.df = _diffsp(self.df, col, serie, name)
    """

    # **************************
    #           charts
    # **************************

    def bokeh(self):
        """
        Use the Bokeh charts engine

        :example: `ds.bokeh()`
        """
        self._charts.engine = "bokeh"

    def altair(self):
        """
        Use the Altair charts engine

        :example: `ds.altair()`
        """
        self._charts.engine = "altair"

    def axis(self, x_axis_col: str, y_axis_col: str):
        """
        Set the columns to use for the chart x and y axis

        :param x_axis_col: name of the column to use for x axis chart
        :type x_axis_col: str
        :param y_axis_col: name of the column to use for y axis chart
        :type y_axis_col: str

        :example: `ds.axis("col1", "col2")`
        """
        self._charts.set_axis(x_axis_col, y_axis_col)

    def line_(self, *args, **kwargs) -> ChartType:
        """
        Draw a line chart

        :param x_axis_col: name of the column to use for x axis chart, defaults
            to the x axis value set by ds.axis
        :type x_axis_col: Optional[str]
        :param y_axis_col: name of the column to use for y axis chart, defaults
            to the y axis value set by ds.axis
        :type y_axis_col: Optional[str]
        :rtype: an Altair or Bokeh chart

        :example: `ds.line_()`
        """
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "line", *args, **kwargs)

    def point_(self, *args, **kwargs) -> ChartType:
        """
        Draw a point chart

        :rtype: Bokeh or Altair chart

        :example: `ds.point_()`
        """
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "point", *args, **kwargs)

    def bar_(self, *args, **kwargs) -> ChartType:
        """
        Draw a bar chart

        :rtype: Bokeh or Altair chart

        :example: `ds.bar_()`
        """
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "bar", *args, **kwargs)

    def square_(self, *args, **kwargs) -> ChartType:
        """
        Draw a square chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.square_()`
        """
        if self._charts.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "square", *args, **kwargs)

    def rule_(self, *args, **kwargs) -> ChartType:
        """
        Draw a rule chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.rule_()`
        """
        if self._charts.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "rule", *args, **kwargs)

    def tick_(self, *args, **kwargs) -> ChartType:
        """
        Draw a square chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.tick_()`
        """
        if self._charts.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "tick", *args, **kwargs)

    def bar_num_(self, *args, **kwargs) -> ChartType:
        """
        Draw a bar chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.bar_num_()`
        """
        if self._charts.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "bar_num", *args, **kwargs)

    def line_num_(self, *args, **kwargs) -> ChartType:
        """
        Draw a line chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.line_num_()`
        """
        if self._charts.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "line_num", *args, **kwargs)

    def point_num_(self, *args, **kwargs) -> ChartType:
        """
        Draw a point chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.point_num_()`
        """
        if self._charts.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "point_num", *args, **kwargs)

    def area_(self, *args, **kwargs) -> ChartType:
        """
        Draw an area chart

        :rtype: Bokeh or Altair chart

        :example: `ds.area_()`
        """
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "area", *args, **kwargs)

    def heatmap_(self, *args, **kwargs) -> ChartType:
        """
        Draw a heatmap chart

        :rtype: Bokeh or Altair chart

        :example: `ds.heatmap_()`
        """
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "heatmap", *args, **kwargs)

    def hist_(self, *args, **kwargs) -> ChartType:
        """
        Draw a histogram chart

        :rtype: Bokeh or Altair chart

        :example: `ds.hist_()`
        """
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "hist", *args, **kwargs)

    def hline_(self, *args, **kwargs) -> ChartType:
        """
        Draw an horizontal mean line for the y axis

        :rtype: Bokeh or Altair chart

        :example: `ds.hline_()`
        """
        df = self.df.to_pandas()
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._charts.chart(df, "hline", *args, **kwargs)

    def w(self, v: int):
        """
        Set the default width of charts

        :param v: the width to set, in pixel
        :type v: int

        :example: `ds.w(350)`
        """
        self._charts.width(v)

    def h(self, v: int):
        """
        Set the default width of charts

        :param v: the height to set, in pixel
        :type v: int

        :example: `ds.h(250)`
        """
        self._charts.height(v)

    def wh(self, w: int, h: int):
        """
        Set the default width and height of charts

        :param w: the height to set, in pixel
        :type w: int
        :param h: the height to set, in pixel
        :type h: int

        :example: `ds.wh(500, 200)`
        """
        self._charts.wh(w, h)

    # **************************
    #           export
    # **************************

    def export_csv(self, filepath: str, **kwargs):
        """
        Write the main dataframe to a csv file

        :param filepath: path of the file to save
        :type filepath: str
        :param **kwargs: arguments to pass to ``pd.to_csv``

        :example: `ds.export_csv("myfile.csv", header=false)`
        """
        return export_csv(self.df, filepath, **kwargs)

    def report_path(self, path: str):
        """Set the report path folder

        :param path: the path where to save reports: relative or absolute
        :type path: str

        :example: `ds.report_path("../reports")`
        """
        self._reports.path = path

    def stack(
        self,
        chart: ChartType,
        title: Optional[str] = None,
        description: Optional[str] = None,
    ):
        """Store a chart in the report stack

        :param chart: a chart object
        :type chart: ChartType
        :param title: the chart title, defaults to None
        :type title: Optional[str], optional
        :param description: the chart description, defaults to None
        :type description: Optional[str], optional
        """
        self._reports.stack(chart, self._charts.engine, title, description)
        m = "" if not title else title + " "
        msg_info(f"Chart {m}added in the report stack")

    def save_pdf(self, filename: str, clear_stack=True):
        """Save a report to a pdf file

        :param filename: the filename
        :type filename: str
        :param clear_stack: clear the reporting stack, defaults to True
        :type clear_stack: bool, optional
        """
        self._reports.save_pdf(filename, clear_stack)
        msg_ok("Pdf file saved")

    def save_html(self, info=False, clear_stack=True):
        """Save a report to multiple html files, one per stacked item

        :param info: print info about the html headers, defaults to False
        :type info: bool, optional
        :param clear_stack: clear the reporting stack, defaults to True
        :type clear_stack: bool, optional
        """
        self._reports.save_html(info, clear_stack)
