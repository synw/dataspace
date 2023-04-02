import polars as pl


def _lreg2(df, xcol, ycol, name):
    n = df.shape[0]

    # Calculate means
    mean_x = df[xcol].sum() / n
    mean_y = df[ycol].sum() / n

    # Calculate the numerator and denominator for the slope (b1) and intercept (b0)
    numer = (pl.col(xcol) * pl.col(ycol)).sum() - n * pl.col(xcol).mean() * pl.col(
        ycol
    ).mean()
    denom = (pl.col(xcol) * pl.col(xcol)).sum() - n * pl.col(xcol).mean() * pl.col(
        xcol
    ).mean()

    # Calculate slope and intercept
    b1 = numer / denom
    b0 = mean_y - b1 * mean_x

    # Calculate predictions and add them as a new column
    predictions = b0 + b1 * pl.col(xcol)
    df = df.with_column(predictions.alias(name))

    return df


def _lreg(df: pl.DataFrame, xcol: str, ycol: str, name: str = "Regression"):
    """
    Adds a regression column to the main dataframe using linear regression.

    Args:
        xcol (str): The name of the column containing the x values.
        ycol (str): The name of the column containing the y values.
        name (str, optional): The name of the resulting regression column. Defaults to "Regression".
    """
    # Convert columns to lists
    x = df[xcol].to_list()
    y = df[ycol].to_list()

    # Calculate means
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    # Calculate the numerator and denominator for the slope (b1) and intercept (b0)
    numer = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))])
    denom = sum([(x[i] - mean_x) ** 2 for i in range(len(x))])

    # Calculate slope and intercept
    b1 = numer / denom
    b0 = mean_y - b1 * mean_x

    # Calculate predictions and add them as a new column
    predictions = [b0 + b1 * x[i] for i in range(len(x))]
    return df.with_columns(pl.Series(name=name, values=predictions))
