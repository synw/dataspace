import platform

try:
    from IPython import get_ipython  # type: ignore
except ImportError:
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


is_running_in_browser = platform.system() == "Emscripten"
is_notebook = _is_notebook()
