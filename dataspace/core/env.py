try:
    from IPython import get_ipython
except:
    pass


def _is_notebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True
        else:
            return False
    except NameError:
        return False


is_notebook = _is_notebook()
