import json

from docsource.docparser import parse_class, parse_docstrings, get_examples


def parse_core():
    methods = parse_class("dataspace", "DataSpace")
    doc = parse_docstrings(methods)
    del doc["__init__"]
    del doc["__repr__"]
    print("Writing doc ref")
    file = "src/autodoc/docref.json"
    with open(file, "w") as filetowrite:
        filetowrite.write(json.dumps(doc))


def parse_examples():
    print("Writing examples ref")
    efile = "src/autodoc/exref.json"
    examples = get_examples("docsource/examples.py")
    with open(efile, "w") as filetowrite:
        filetowrite.write(json.dumps(examples))


def parse_chart_classes():
    alt = parse_class("dataspace.charts.altair", "Chart")
    doc = parse_docstrings(alt)
    print("Writing chart options doc ref")
    file = "src/autodoc/chartsref.json"
    with open(file, "w") as filetowrite:
        filetowrite.write(json.dumps(doc))


def main():
    parse_core()
    parse_examples()
    parse_chart_classes()


if __name__ == "__main__":
    main()
