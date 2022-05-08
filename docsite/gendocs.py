import ast
import inspect
import json
from importlib import import_module
from docstring_parser import parse, Docstring
from typing import TypedDict


MethodsDict = TypedDict("name", {"funcdef": str, "docstring": Docstring})


def _parseClass(mod: str, cls: str) -> MethodsDict:
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


def get_examples():
    pass


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
            "params": params,
            "raises": raises,
            "return": r,
        }
    return docs


# methods = get_methods()
methods = _parseClass("dataspace", "DataSpace")
doc = parse_docstrings(methods)
# del doc["__init__"]
# del doc["__repr__"]
# res = doc["wunique_"]
# print(json.dumps(res, indent=4))
print("Writing doc ref")
file = "src/autodoc/docref.json"
with open(file, "w") as filetowrite:
    filetowrite.write(json.dumps(doc))
