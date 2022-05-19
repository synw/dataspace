import json

from docsource.docparser import parse_class, parse_docstrings, get_examples


def main():
    # methods = get_methods()
    methods = parse_class("dataspace", "DataSpace")
    doc = parse_docstrings(methods)
    del doc["__init__"]
    del doc["__repr__"]
    print("Writing doc ref")
    file = "src/autodoc/docref.json"
    with open(file, "w") as filetowrite:
        filetowrite.write(json.dumps(doc))
    print("Writing examples ref")
    efile = "src/autodoc/exref.json"
    examples = get_examples("docsource/examples.py")
    with open(efile, "w") as filetowrite:
        filetowrite.write(json.dumps(examples))


if __name__ == "__main__":
    main()
