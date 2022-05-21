from typing import Dict, List, Optional

import pandas as pd
from dataspace.calculations import _diffm, _diffn, _diffp  # _diffs, _diffsp
from dataspace.charts import DsChart
from dataspace.clean import (
    _drop_nan,
    _fdate,
    _fill_nan,
    _fill_nulls,
    _replace,
    _roundvals,
    _strip,
    _strip_cols,
    _timestamps,
    _to_date,
    _to_float,
    _to_int,
    _to_type,
)
from dataspace.core.env import is_notebook
from dataspace.count import _count_empty_, _count_null_, _count_unique_, _count_zero_
from dataspace.info import _cols
from dataspace.info.view import _show
from dataspace.io.export import _export_csv
from dataspace.transform import _append, _apply, _drop, _rename, _rmean, _rsum
from dataspace.utils.messages import msg_ok
from numpy import nan


class DataSpace:
    df: pd.DataFrame = None
    _chartEngine: DsChart = DsChart()

    def __init__(self, df: pd.DataFrame = None) -> None:
        self.df = df

    def __repr__(self) -> str:
        num = 0
        if self.df is not None:
            num = len(self.df.index)
        msg = "<DataSpace object | " + str(num) + " rows>"
        if is_notebook is True:
            self.df.head()
            return str(self.df.head(5))
        return msg

    # **************************
    #           info
    # **************************

    def show(self, rows: int = 5) -> pd.DataFrame:
        """
        Display info about the dataframe

        Category: Info/View data/Show

        :param rows: number of rows to show, **default**: 5
        :type rows: ``int`` *optional*
        :return: a pandas dataframe head
        :rtype: ``DataFrame``

        :example: `ds.show()`
        """
        return _show(rows, self.df)

    def cols_(self) -> pd.DataFrame:
        """
        Returns a dataframe with columns info

        Category: Info/View data/Show

        :return: a pandas dataframe
        :rtype: ``DataFrame``

        :example: `ds.cols_()`
        """
        return _cols(self.df)

    # **************************
    #           clean
    # **************************

    def to_date(self, *cols: str, **kwargs) -> None:
        """
        Convert some columns values to date type

        Category: Clean/Dates/To date

        :param cols: names of the colums
        :type cols: str *at least one*
        :param \\*\\*kwargs: keyword arguments for ``pd.to_datetime``
        :type \\*\\*kwargs: optional

        :example: `ds.to_date("mycol")`
        """
        _to_date(self.df, *cols, **kwargs)

    def to_int(self, *cols: str, **kwargs) -> None:
        """
        Convert some column values to integers

        Category: Clean/Convert types/To type

        :param \\*cols: names of the columns
        :type \\*cols: str *at least one*
        :param \\*\\*kwargs: keyword arguments for ``pd.to_numeric``
        :type \\*\\*kwargs: optional

        :example: `ds.to_int("mycol1", "mycol2", errors="coerce")`
        """
        _to_int(self.df, *cols, **kwargs)
        if is_notebook is True:
            msg_ok("Converted columns values to integers")

    def to_float(self, *cols: str, **kwargs) -> None:
        """
        Convert colums values to float -

        Category: Clean/Convert types/To float

        :param cols: name of the columns
        :type cols: str *at least one*
        :param \\*\\*kwargs: keyword arguments for ``df.astype``
        :type \\*\\*kwargs: optional

        :example: `ds.to_float("mycol1")`
        """
        _to_float(self.df, *cols, **kwargs)
        if is_notebook is True:
            msg_ok("Converted columns values to floats")

    def to_type(self, dtype: type, *cols: str, **kwargs) -> None:
        """
        Convert colums values to a given type in the main dataframe

        Category: Clean/Convert types/To type

        :param dtype: a type to convert to: ex: str
        :type dtype: ``type``
        :param \\*cols: names of the columns
        :type \\*cols: str *at least one**
        :param \\*\\*kwargs: keyword arguments for ``df.astype``
        :type \\*\\*kwargs: optional

        :examples: ``ds.to_type(str, "mycol")``
        """
        _to_type(self.df, dtype, *cols, **kwargs)
        if is_notebook is True:
            msg_ok(f"Converted columns values to {dtype}")

    def drop_nan(self, col: str, method: str = "all", **kwargs) -> None:
        """
        Drop rows with ``NaN`` values from the main dataframe

        :param col: name of the column
        :type col: str *optional*
        :param method: ``how`` param for ``df.dropna``, **default**: "all"
        :type method: str *optional*
        :param \\*\\*kwargs: params for ``df.dropna``
        :type \\*\\*kwargs: optional

        :example: `ds.drop_nan("mycol")`
        """
        self.df = _drop_nan(self.df, col, method, **kwargs)

    def fill_nan(self, val: str, *cols):
        """
        Fill NaN values with new values in the main dataframe

        :param val: new value
        :type val: str
        :param \\*cols: names of the colums
        :type \\*cols: str *at least one*

        :example: ``ds.fill_nan("new value", "mycol1", "mycol2")``
        """
        self.df = _fill_nan(self.df, val, *cols)

    def fill_nulls(self, val=nan, *cols: str, nulls=[None, ""]):
        """
        Fill all null values with NaN values in a column.

        Null values are ``None`` or en empty string

        :param cols: columns names
        :type cols: str *at least one*

        :example: `ds.fill_nulls("mycol")`
        """
        self.df = _fill_nulls(self.df, val, *cols, nulls=nulls)

    def index(self, col: str) -> pd.DataFrame:
        """
        Set an index to the main dataframe

        :param col: column name where to index from
        :type col: str

        :example: `ds.index("mycol")`
        """
        self.df.set_index(self.df[col], inplace=True)

    def dateindex(self, col: str) -> pd.DataFrame:
        """
        Set a datetime index from a column

        :param col: column name where to index the date from
        :type col: str

        :example: `ds.dateindex("mycol")`
        """
        index = pd.DatetimeIndex(self.df[col])
        self.df.set_index(index, inplace=True)

    def fdate(self, *cols, precision: str = "S", format: Optional[str] = None):
        """
        Convert column values to formated date string

        :param \\*cols: names of the colums
        :type \\*cols: str, at least one
        :param precision: time precision: Y, M, D, H, Min S, defaults to "S"
        :type precision: str *optional*
        :param format: python date format, defaults to None
        :type format: str, optional

        :example: `ds.fdate("mycol1", "mycol2", precision="D")`
        """
        _fdate(self.df, *cols, precision=precision, format=format)

    def timestamps(self, col: str, **kwargs):
        """
        Add a timestamps column from a date column

        :param col: name of the timestamps column to add
        :type col: str
        :param \\*\\*kwargs: keyword arguments for ``pd.to_datetime``
        :type \\*\\*kwargs: optional

        :example: ``ds.timestamps("mycol")``
        """
        _timestamps(self.df, col, **kwargs)

    def strip(self, *cols: str):
        """
        Remove leading and trailing white spaces column's values

        :param col: name of the column
        :type col: str

        :example: `ds.strip("mycol")`
        """
        _strip(self.df, *cols)

    def strip_cols(self):
        """
        Remove leading and trailing white spaces in columns names

        :example: `ds.strip_cols()`
        """
        _strip_cols(self.df)

    def roundvals(self, col: str, precision: int = 2):
        """
        Round floats in a column. Numbers are going to be
        converted to floats if they are not already

        :param col: column name
        :type col: str
        :param precision: float precision, defaults to 2
        :param precision: ``int`` *optional*

        :example: `ds.roundvals("mycol")`
        """
        _roundvals(self.df, col, precision)

    def replace(self, col: str, searchval: str, replaceval: str):
        """
        Replace a value in a column in the main dataframe

        :param col: column name
        :type col: str
        :param searchval: value to replace
        :type searchval: str
        :param replaceval: new value
        :type replaceval: str

        :example: `ds.replace("mycol", "value", "new_value")`
        """
        _replace(self.df, col, searchval, replaceval)

    # **************************
    #           select
    # **************************

    def limit(self, r: int = 5) -> None:
        """
        Limit selection to a range in the main dataframe

        :param r: number of rows to keep, **default**: 5
        :type r: ``int`` *optional*

        :example: `ds.limit(100)`
        """
        self.df = self.df[:r]

    def unique_(self, col: str) -> List[str]:
        """
        Returns a list of unique values in a column

        :param col: the column to select from
        :type col: str
        :return: a list of unique values in the column
        :rtype: ``List[str]``

        :example: `ds.unique_("col1")`
        """
        try:
            df = self.df.drop_duplicates(subset=[col], inplace=False)
            return list(df[col])
        except Exception as e:
            raise Exception("Can not select unique data", e)

    def wunique_(self, col: str, colname: str = "Number") -> pd.DataFrame:
        """
        Weight unique values: returns a dataframe with a count
        of unique values for a column

        :param col: the column to select from
        :type col: str
        :return: a dataframe with a count of unique values in the column
        :rtype: ``pd.DataFrame``

        :example: `ds.wunique_("col1")`
        """
        try:
            s = pd.value_counts(self.df[col].values)
            df = pd.DataFrame(s, columns=[colname])
            return df
        except Exception as e:
            raise Exception("Can not weight unique data", e)

    # **************************
    #           count
    # **************************

    def count_null_(self, col: str) -> int:
        """Count the number of null values in a column

        :param col: the column to count from
        :type col: str
        :return: number of values
        :rtype: int

        :example: `ds.count_nulls_("col1")`
        """
        return _count_null_(self.df, col)

    def count_empty_(self, col: str) -> int:
        """List of empty row indices

        :param col: column to count from
        :type col: str
        :return: number of values
        :rtype: int

        :example: `ds.count_empty_("col1")`
        """
        return _count_empty_(self.df, col)

    def count_zero_(self, col: str) -> int:
        """List of row with 0 values

        :param col: column to count from
        :type col: str
        :return: number of values
        :rtype: int

        :example: `ds.count_zero_("col1")`
        """
        return _count_zero_(self.df, col)

    def count_unique_(self, col: str) -> int:
        """Return the number of unique values in a column

        :param col: column to count from
        :type col: str
        :return: number of unique values
        :rtype: int

        :example: `ds.count_unique_("col1")`
        """
        return _count_unique_(self.df, col)

    # **************************
    #        transform
    # **************************

    def split_(self, col: str) -> Dict[str, "DataSpace"]:
        """
        Split the main dataframe according to a column's unique values and
        return a dict of DataSpace instances

        :return: list of DataSpace instances
        :rtype: ``List[DataSpace]``

        :example: `dss = ds.slit_("Col 1")`
        """
        dss = {}
        try:
            unique = self.df[col].unique()
            for key in unique:
                df2 = DataSpace(self.df.loc[self.df[col] == key])
                dss[key] = df2
        except Exception as e:
            raise Exception("Can not split dataframe", e)
        return dss

    def sort(self, col: str, **kwargs):
        """
        Sorts the main dataframe according to the given column

        :param col: column name
        :type col: str

        :example: `ds.sort("Col 1")`
        """
        try:
            self.df = self.df.sort_values(col, **kwargs)
        except Exception as e:
            raise Exception("Can not sort the dataframe from column ", col, e)

    def indexcol(self, col: str):
        """
        Add a column from the index

        :param col: name of the new column
        :type col: str

        :example: ``ds.index_col("New col")``
        """
        try:
            self.df[col] = self.df.index.values
        except Exception as e:
            raise e
        if is_notebook is True:
            msg_ok("Column", col, "added from the index")

    def drop(self, *cols) -> None:
        """
        Drops columns from the main dataframe

        :param cols: names of the columns
        :type cols: str

        :example: ``ds.drop("Col 1", "Col 2")``
        """
        self.df = _drop(self.df, *cols)

    def rename(self, source_col: str, dest_col: str) -> None:
        """
        Renames a column in the main dataframe

        :param source_col: name of the column to rename
        :type source_col: str
        :param dest_col: new name of the column
        :type dest_col: str

        :example: ``ds.rename("Col 1", "New col")``
        """
        self.df = _rename(self.df, source_col, dest_col)

    def add(self, col: str, value) -> None:
        """
        Add a column with default values

        :param col: column name
        :type col: str
        :param value: column value
        :type value: any

        :example: ``ds.add("Col 4", 0)``
        """
        try:
            self.df[col] = value
        except Exception as e:
            raise Exception("Can not add column", e)

    def keep(self, *cols) -> None:
        """
        Limit the dataframe to some columns

        :param cols: names of the columns
        :type cols: str

        :example: ``ds.keep("Col 1", "Col 2")``
        """
        try:
            self.df = self.df[list(cols)]
        except Exception as e:
            raise Exception("Can not remove colums", e)
        msg_ok("Setting dataframe to columns", " ".join(cols))

    def exclude(self, col: str, val) -> None:
        """
        Delete rows based on value

        :param col: column name
        :type col: str
        :param val: value to delete
        :type val: any

        :example: ``ds.exclude("Col 1", "value")``
        """
        try:
            self.df = self.df[self.df[col] != val]
        except Exception as e:
            raise Exception("Can not exclude rows based on value " + str(val), e)

    def copycol(self, origin_col: str, dest_col: str):
        """
        Copy a columns values in another column

        :param origin_col: name of the column to copy
        :type origin_col: str
        :param dest_col: name of the new column
        :type dest_col: str

        :example: ``ds.copy("col 1", "New col")``
        """
        try:
            self.df[dest_col] = self.df[[origin_col]]
        except Exception as e:
            raise Exception("Can not copy column", e)

    def dropr(self, *rows):
        """
        Drops some rows from the main dataframe

        :param rows: rows names
        :type rows: list of ints

        :example: ``ds.drop_rows([0, 2])``
        """
        try:
            self.df = self.df.drop(*rows)
        except Exception as e:
            raise Exception("Can not drop rows", e)
        msg_ok("Rows dropped")

    def append(self, *vals, ignore_index=True) -> None:
        """
        Append a row to the main dataframe

        :param vals: list of the row values to add
        :type vals: list
        :param index: index key, defaults to None
        :param index: any, optional

        :example: ``ds.append([0, 2, 2, 3, 4])``
        """
        self.df = _append(self.df, *vals, ignore_index=ignore_index)

    def reverse(self) -> None:
        """
        Reverses the main dataframe order

        :example: ``ds.reverse()``
        """
        try:
            self.df = self.df.iloc[::-1]
        except Exception as e:
            raise Exception("Can not reverse the dataframe", e)

    def apply(self, function, *cols: List[str], axis=1, **kwargs) -> None:
        """
        Apply a function on columns values

        :param function: a function to apply to the columns
        :type function: function
        :param cols: columns names
        :type cols: name of columns
        :param axis: index (0) or column (1), default is 1
        :param kwargs: arguments for ``df.apply``
        :type kwargs: optional

        :example:
                        .. code-block:: python

                                def f(row):
                                        # add a new column with a value
                                        row["newcol"] = row["col1"] + 1
                                        return row

                                ds.apply(f)

        """
        self.df = _apply(self.df, function, *cols, axis=axis, **kwargs)

    def rsum(
        self, time_period: str, num_col: str = "Number", dateindex: Optional[str] = None
    ) -> None:
        """
        Resample and add a sum the main dataframe to a time period

        :param time_period: unit + period: periods are Y, M, D, H, Min, S
        :param time_period: str
        :param num_col: name of the new column, defaults to "Number"
        :param num_col: str, optional
        :param dateindex: column name to use as date index, defaults to None
        :param dateindex: str, optional

        :example: ``ds.rsum("1D")``
        """
        self.df = _rsum(self.df, time_period, num_col, dateindex)

    def rmean(
        self, time_period: str, num_col: str = "Number", dateindex: Optional[str] = None
    ):
        """
        Resample and add a sum column the main dataframe to a time period

        :param time_period: unit + period: periods are Y, M, D, H, Min, S
        :param time_period: str
        :param num_col: number of the new column, defaults to "Number"
        :param num_col: str, optional
        :param dateindex: column name to use as date index, defaults to None

        :example: ``ds.rmean("1Min")``
        """
        self.df = _rmean(self.df, time_period, num_col, dateindex)

    # **************************
    #        calculations
    # **************************

    def percent(self, col: str, roundn=1):
        """add a percent column

        :param col: the column to calculate percentages from
        :type col: str
        :param roundn: round level, defaults to 1
        :type roundn: int, optional

        :example: ``ds.percent("amount")``
        """
        self.df["percent"] = round((self.df[col] / self.df[col].sum()) * 100, roundn)

    def diffn(self, diffcol: str, name: str = "Diff", doround=True) -> None:
        """
        Add a diff column to the main dataframe: calculate the diff
        from the next value

        :param diffcol: column to diff from
        :type diffcol: str
        :param name: diff column name, defaults to "Diff"
        :type name: str, optional

        :example: ``ds.diffn("Col 1", "New col")``
        """
        self.df = _diffn(
            self.df, diffcol=diffcol, name=name, doround=doround, percent=False
        )

    def diffnp(self, diffcol: str, name: str = "Diff", doround=True) -> None:
        """
        Add a diff column to the main dataframe: calculate the diff
        in percentage from the next value

        :param diffcol: column to diff from
        :type diffcol: str
        :param name: diff column name, defaults to "Diff"
        :type name: str, optional

        :example: ``ds.diffnp("Col 1", "New col")``
        """
        self.df = _diffn(
            self.df, diffcol=diffcol, name=name, doround=doround, percent=True
        )

    def diffp(self, diffcol: str, name: str = "Diff", doround=True) -> None:
        """
        Add a diff column to the main dataframe: calculate the diff
        from the previous value

        :param diffcol: column to diff from
        :type diffcol: str
        :param name: diff column name, defaults to "Diff"
        :type name: str, optional

        :example: ``ds.diffp("Col 1", "New col")``
        """
        self.df = _diffp(
            self.df, diffcol=diffcol, name=name, doround=doround, percent=False
        )

    def diffpp(self, diffcol: str, name: str = "Diff", doround=True) -> None:
        """
        Add a diff column to the main dataframe: calculate the diff
        in percentage from the previous value

        :param diffcol: column to diff from
        :type diffcol: str
        :param name: diff column name, defaults to "Diff"
        :type name: str, optional

        :example: ``ds.diffpp("Col 1", "New col")``
        """
        self.df = _diffp(
            self.df, diffcol=diffcol, name=name, doround=doround, percent=True
        )

    def diffm(
        self, diffcol: str, name: str = "Diff", default=nan, doround=True
    ) -> None:
        """
        Add a diff column to the main dataframe: calculate the
        diff from the column mean

        :param diffcol: column to diff from
        :type diffcol: str
        :param name: diff column name, defaults to "Diff"
        :param name: str, optional
        :param default: column default value, defaults to nan
        :param default: optional

        :example: ``ds.diffm("Col 1", "New col")``
        """
        self.df = _diffm(
            self.df, diffcol, name=name, default=default, doround=doround, percent=False
        )

    def diffmp(
        self, diffcol: str, name: str = "Diff", default=nan, doround=True
    ) -> None:
        """
        Add a diff column to the main dataframe: calculate the
        diff in percentage from the column mean

        :param diffcol: column to diff from
        :type diffcol: str
        :param name: diff column name, defaults to "Diff"
        :param name: str, optional
        :param default: column default value, defaults to nan
        :param default: optional

        :example: ``ds.diffmp("Col 1", "New col")``
        """
        self.df = _diffm(
            self.df, diffcol, name=name, default=default, doround=doround, percent=True
        )

    """
    def diffs(self, col: str, serie: Iterable, name: str = "Diff") -> None:
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

    def diffsp(self, col: str, serie: Iterable, name: str = "Diff") -> None:
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

    def bokeh(self) -> None:
        """
        Use the Bokeh charts engine

        :example: `ds.bokeh()`
        """
        self._chartEngine.engine = "bokeh"

    def altair(self) -> None:
        """
        Use the Altair charts engine

        :example: `ds.altair()`
        """
        self._chartEngine.engine = "altair"

    def axis(self, x_axis_col: str, y_axis_col: str):
        """
        Set the columns to use for the chart x and y axis

        :param x_axis_col: name of the column to use for x axis chart
        :type x_axis_col: str
        :param y_axis_col: name of the column to use for y axis chart
        :type y_axis_col: str

        :example: `ds.axis("col1", "col2")`
        """
        self._chartEngine.set_axis(x_axis_col, y_axis_col)

    def line_(self, *args, **kwargs):
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
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "line", *args, **kwargs)

    def point_(self, *args, **kwargs):
        """
        Draw a point chart

        :rtype: Bokeh or Altair chart

        :example: `ds.point_()`
        """
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "point", *args, **kwargs)

    def bar_(self, *args, **kwargs):
        """
        Draw a bar chart

        :rtype: Bokeh or Altair chart

        :example: `ds.bar_()`
        """
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "bar", *args, **kwargs)

    def square_(self, *args, **kwargs):
        """
        Draw a square chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.square_()`
        """
        if self._chartEngine.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "square", *args, **kwargs)

    def rule_(self, *args, **kwargs):
        """
        Draw a rule chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.rule_()`
        """
        if self._chartEngine.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "rule", *args, **kwargs)

    def tick_(self, *args, **kwargs):
        """
        Draw a square chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.tick_()`
        """
        if self._chartEngine.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "tick", *args, **kwargs)

    def bar_num_(self, *args, **kwargs):
        """
        Draw a bar chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.bar_num_()`
        """
        if self._chartEngine.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "bar_num", *args, **kwargs)

    def line_num_(self, *args, **kwargs):
        """
        Draw a line chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.line_num_()`
        """
        if self._chartEngine.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "line_num", *args, **kwargs)

    def point_num_(self, *args, **kwargs):
        """
        Draw a point chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.point_num_()`
        """
        if self._chartEngine.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "point_num", *args, **kwargs)

    def area_(self, *args, **kwargs):
        """
        Draw an area chart

        :rtype: Bokeh or Altair chart

        :example: `ds.area_()`
        """
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "area", *args, **kwargs)

    def heatmap_(self, *args, **kwargs):
        """
        Draw a heatmap chart

        :rtype: Bokeh or Altair chart

        :example: `ds.heatmap_()`
        """
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "heatmap", *args, **kwargs)

    def hist_(self, *args, **kwargs):
        """
        Draw a histogram chart

        :rtype: Bokeh or Altair chart

        :example: `ds.hist_()`
        """
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "hist", *args, **kwargs)

    def hline_(self, *args, **kwargs):
        """
        Draw an horizontal mean line for the y axis

        :rtype: Bokeh or Altair chart

        :example: `ds.hline_()`
        """
        df = self.df
        if "df" in kwargs.keys():
            df = kwargs["df"]
        return self._chartEngine.chart(df, "hline", *args, **kwargs)

    def w(self, v: int):
        """
        Set the default width of charts

        :param v: the width to set, in pixel
        :type v: int

        :example: `ds.w(350)`
        """
        self._chartEngine.width(v)

    def h(self, v: int):
        """
        Set the default width of charts

        :param v: the height to set, in pixel
        :type v: int

        :example: `ds.h(250)`
        """
        self._chartEngine.height(v)

    def wh(self, w: int, h: int):
        """
        Set the default width and height of charts

        :param w: the height to set, in pixel
        :type w: int
        :param h: the height to set, in pixel
        :type h: int

        :example: `ds.wh(500, 200)`
        """
        self._chartEngine.wh(w, h)

    # **************************
    #           export
    # **************************

    def export_csv(self, filepath: str, **kwargs) -> None:
        """
        Write the main dataframe to a csv file

        :param filepath: path of the file to save
        :type filepath: str
        :param \\*\\*kwargs: arguments to pass to ``pd.to_csv``

        :example: `ds.export_csv("myfile.csv", header=false)`
        """
        return _export_csv(self.df, filepath, **kwargs)
