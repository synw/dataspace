import pandas as pd

from dataspace.utils.messages import msg_start, msg_end, msg_warning
from . import DataSpace


def _load_csv(url, **kwargs) -> pd.DataFrame:
    msg_start("Loading csv...")
    try:
        return pd.read_csv(url, **kwargs)
    except FileNotFoundError:
        msg = "File " + url + " not found"
        msg_warning(msg)
        return
    except Exception as e:
        raise Exception("Can not load csv file", e)
    msg_end("Finished loading csv")


def _load_django(query) -> pd.DataFrame:
    try:
        df = pd.DataFrame(list(query.values()))
        return df
    except Exception as e:
        raise Exception("Can not create dataspace from query", e)


def from_df(df: pd.DataFrame) -> DataSpace:
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
