import platform
import builtins

try:
    from IPython import get_ipython
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


def bprint(*args, **kwargs):
    builtins.print("#!S#")
    builtins.print(*args, **kwargs)
    builtins.print("#!E#")


# if is_running_in_browser:
#    print = bprint
