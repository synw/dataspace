import json
from docdundee.docparser import (
    parse_class,
    parse_docstrings,
    parse_functions,
    write_docstrings,
    get_func_sources,
)


def parse_core():
    methods = parse_class("dataspace", "DataSpace")
    doc = parse_docstrings(methods)
    del doc["__init__"]
    del doc["__repr__"]
    print("Writing doc ref")
    file = "docsite/public/doc/api/docstrings.json"
    write_docstrings(file, doc)


def parse_examples():
    print("Writing examples ref")
    efile = "src/autodoc/exref.json"
    examples = get_func_sources("docsource/examples.py")
    with open(efile, "w") as filetowrite:
        filetowrite.write(json.dumps(examples))


def parse_chart_classes():
    alt = parse_class("dataspace.charts.altair.charts", "AltairChart")
    doc = parse_docstrings(alt)
    print("Writing chart options doc ref")
    file = "docsite/public/doc/doc/charts/inline_api/docstrings.json"
    write_docstrings(file, doc)


def parse_funcs():
    alt = parse_functions("dataspace.core.load", mode="private")
    doc = parse_docstrings(alt)
    print("Writing top level functions doc ref")
    file = "docsite/public/doc/doc/data_io/load/docstrings.json"
    write_docstrings(file, doc)


def main():
    parse_core()
    # parse_examples()
    parse_chart_classes()
    parse_funcs()


if __name__ == "__main__":
    main()
