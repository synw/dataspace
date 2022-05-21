import ast
import inspect
from docutils.core import publish_parts
from importlib import import_module
from docstring_parser import parse, Docstring
from typing import Tuple, TypedDict, Union


MethodsDict = TypedDict("name", {"funcdef": str, "docstring": Docstring})
ExamplesDict = TypedDict("name", {"source": str})


def rst_to_html(txt: str) -> str:
    return (
        publish_parts(
            txt,
            settings_overrides={"output_encoding": "unicode"},
            writer_name="html",
        )["body"]
        .replace("<p>", "")
        .replace("</p>", "")
    )


def parse_nodes(source: str, nodes) -> MethodsDict:
    i = 0
    methods: MethodsDict = {}  # type: ignore
    for node in nodes:  # type: ignore
        if isinstance(node, ast.FunctionDef):
            s = ast.get_source_segment(source, node)  # type: ignore
            d = s.split("\n")[0].replace("    ", "")  # type: ignore
            methods[node.name] = {
                "funcdef": d[:-1],
                "docstring": parse(ast.get_docstring(node) or ""),
            }
        i += 1
    return methods


def parse_class(mod: str, cls: str) -> MethodsDict:
    source = inspect.getsource(getattr(import_module(mod), cls))
    _mod = ast.parse(source)
    _cls = _mod.body[0]
    return parse_nodes(source, _cls.body)  # type: ignore


def parse_functions(mod: str) -> MethodsDict:
    source = inspect.getsource(import_module(mod))
    _mod = ast.parse(source)
    return parse_nodes(source, _mod.body)  # type: ignore


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


def parse_long_description(
    desc: Union[str, None]
) -> Tuple[Union[str, None], Union[str, None]]:
    if desc is None:
        return (desc, None)
    sl = desc.split(".. code-block:: python\n\n")
    if len(sl) < 2:
        return (desc, None)
    _desc = sl[0]
    _ex = sl[1].replace("  ", "")
    return (_desc, _ex)


def parse_docstrings(methods: MethodsDict):
    docs = {}
    for k in methods.keys():
        params = {}
        raises = {}
        method = methods[k]
        for param in method["docstring"].params:
            pdesc = param.description
            ptype = param.type_name
            pdefault = param.default
            if pdesc is not None:
                pdesc = rst_to_html(pdesc)
            if ptype is not None:
                ptype = rst_to_html(ptype)
            if pdefault is not None:
                pdefault = rst_to_html(pdefault)
            params[param.arg_name] = {
                "description": pdesc,
                "type": ptype,
                # "is_optional": param.is_optional,
                "default": pdefault,
            }
        for ex in method["docstring"].raises:
            raises[ex.type_name] = ex.description
        r = {"name": None, "type": None}
        if method["docstring"].returns is not None:
            rn = method["docstring"].returns.return_name
            if rn is not None:
                rn = rst_to_html(rn)
            rt = method["docstring"].returns.type_name
            if rt is not None:
                rt = rst_to_html(rt)
            r["name"] = rn
            r["type"] = rt
        desc, example = parse_long_description(method["docstring"].long_description)
        if desc is not None:
            desc = rst_to_html(desc)
        shortdesc = method["docstring"].short_description
        if shortdesc is not None:
            shortdesc = rst_to_html(shortdesc)
        docs[k] = {
            "funcdef": method["funcdef"],
            "description": shortdesc,
            "long_description": desc,
            "example": example,
            "params": params,
            "raises": raises,
            "return": r,
        }
    return docs
