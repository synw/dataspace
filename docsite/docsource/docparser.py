import ast
import inspect
from importlib import import_module
from docstring_parser import parse, Docstring
from typing import TypedDict


MethodsDict = TypedDict("name", {"funcdef": str, "docstring": Docstring})
ExamplesDict = TypedDict("name", {"source": str})


def parse_class(mod: str, cls: str) -> MethodsDict:
    methods: MethodsDict = {}  # type: ignore
    source = inspect.getsource(getattr(import_module(mod), cls))
    _mod = ast.parse(source)
    _cls = _mod.body[0]
    i = 0
    for node in _cls.body:  # type: ignore
        if isinstance(node, ast.FunctionDef):
            s = ast.get_source_segment(source, _cls.body[i])  # type: ignore
            d = s.split("\n")[0].replace("    ", "")  # type: ignore
            methods[node.name] = {
                "funcdef": d[:-1],
                "docstring": parse(ast.get_docstring(node) or ""),
            }
        i += 1
    return methods


def get_examples(file: str) -> ExamplesDict:
    ex: ExamplesDict = {}  # type: ignore
    with open(file, "r") as fileop:
        lines = fileop.readlines()
        source = "".join(lines)
        _mod = ast.parse(source)
        i = 0
        for node in _mod.body:
            if isinstance(node, ast.FunctionDef) or isinstance(
                node, ast.AsyncFunctionDef
            ):
                rawsource = ast.get_source_segment(source, _mod.body[i])  # type: ignore
                if rawsource is None:
                    raise Exception("Source not found")
                lines = rawsource.split("\n")
                lines.pop(0)
                nlines = []
                for line in lines:
                    nl = line.replace("\t", "", 1)
                    nl = nl.replace("    ", "", 1)
                    nlines.append(nl)
                end = "\n".join(nlines)
                ex[node.name] = end
            i += 1
    return ex


def parse_docstrings(methods: MethodsDict):
    docs = {}
    for k in methods.keys():
        params = {}
        raises = {}
        method = methods[k]
        for param in method["docstring"].params:
            params[param.arg_name] = {
                "description": param.description,
                "type": param.type_name,
                # "is_optional": param.is_optional,
                "default": param.default,
            }
        for ex in method["docstring"].raises:
            raises[ex.type_name] = ex.description
        r = {"name": None, "type": None}
        if method["docstring"].returns is not None:
            r["name"] = method["docstring"].returns.return_name
            r["type"] = method["docstring"].returns.type_name
        docs[k] = {
            "funcdef": method["funcdef"],
            "description": method["docstring"].short_description,
            "long_description": method["docstring"].long_description,
            "params": params,
            "raises": raises,
            "return": r,
        }
    return docs
