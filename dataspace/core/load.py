import polars as pl

from dataspace.utils.messages import msg_start, msg_end, msg_warning
from . import DataSpace


def _load_csv(url, **kwargs) -> pl.LazyFrame:
    msg_start("Loading csv...")
    lf: pl.LazyFrame
    try:
        lf = pl.scan_csv(url, **kwargs)
    except FileNotFoundError:
        msg = "File " + url + " not found"
        msg_warning(msg)
        raise Exception(msg)
    msg_end("Csv file loaded")
    return lf


def _load_django(query) -> pl.DataFrame:
    try:
        df = pl.DataFrame(list(query.values()))
        return df
    except Exception as e:
        raise Exception("Can not create dataspace from query", e)


def from_df(df: pl.DataFrame) -> DataSpace:
    """
    Intialize a DataSpace from a pandas DataFrame

    :param df: a pandas ``DataFrame``
    :return: a DataSpace
    :rtype: ``DataSpace``

    :example: `dataspace.from_df(df)`
    """
    return DataSpace(df)


def from_csv(url, **kwargs) -> DataSpace:
    """
    Loads csv data in the main dataframe

    :param url: url of the csv file to load:
                            can be absolute if it starts with ``/``
                            or relative if it starts with ``./``
    :type url: ``str``
    :param kwargs: keyword arguments to pass to Pandas
                                ``read_csv`` function
    :return: a DataSpace
    :rtype: ``DataSpace``

    :example: `dataspace.from_csv("./myfile.csv")`
    """
    return DataSpace(_load_csv(url, **kwargs))


def from_django(query) -> DataSpace:
    """
    Load the main dataframe from a django orm query

    :param query: django query from a model
    :type query: django query

    :return: a DataSpace
    :rtype: ``DataSpace``

    :example: `dataspace.load_django(Mymodel.objects.all())`
    """
    return DataSpace(_load_django(query))
