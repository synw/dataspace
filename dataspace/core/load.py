import polars as pl

from dataspace.utils.messages import msg_start, msg_end, msg_warning
from . import DataSpace


def _load_csv(url, **kwargs) -> pl.DataFrame:
    msg_start("Loading csv...")
    df: pl.DataFrame
    if "try_parse_dates" not in kwargs.keys():
        kwargs["try_parse_dates"] = True
    if "use_pyarrow" not in kwargs.keys():
        kwargs["use_pyarrow"] = True
    try:
        df = pl.read_csv(url, **kwargs)
    except FileNotFoundError:
        msg = "File " + url + " not found"
        msg_warning(msg)
        raise Exception(msg)
    msg_end("Csv file loaded")
    return df


def _load_django(query) -> pl.DataFrame:
    try:
        df = pl.DataFrame(list(query.values()))
        return df
    except Exception as e:
        raise Exception("Can not create dataspace from query", e)


def from_df(df: pl.DataFrame) -> DataSpace:
    """
    Initializes a DataSpace from a DataFrame.

    Args:
        df (polars.DataFrame): A DataFrame.

    Returns:
        DataSpace: A DataSpace object.

    Example:
        dataspace.from_df(df)
    """
    return DataSpace(df)


def from_csv(url, **kwargs) -> DataSpace:
    """
    Loads CSV data into the main DataFrame.

    Args:
        url (str): The URL of the CSV file to load. Can be absolute if it starts
            with ``/``, or relative if it starts with ``./``.
        **kwargs: Optional keyword arguments to pass to Pandas ``read_csv``
            function.

    Returns:
        DataSpace: A DataSpace object.

    Example:
        dataspace.from_csv("./myfile.csv")
    """
    return DataSpace(_load_csv(url, **kwargs))


def from_django(query) -> DataSpace:
    """
    Loads the main DataFrame from a Django ORM query.

    Args:
        query: A Django query from a model.
        type query: django.db.models.query.QuerySet

    Returns:
        DataSpace: A DataSpace object.

    Example:
        dataspace.load_django(Mymodel.objects.all())
    """
    return DataSpace(_load_django(query))
