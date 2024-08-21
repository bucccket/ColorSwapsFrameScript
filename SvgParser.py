import xmltodict
import xml.etree.cElementTree as ET
from os import walk


def parse_svg(full_filename: str = "SvgTemplate.svg"):
    assert full_filename.endswith(".svg"), "File must be an SVG file"

    with open(full_filename, "r") as svg:
        filename = full_filename[:-4] # "import/ExampleName" 
        root = ET.Element("ColorSchemeTypes")
        doc = ET.SubElement(root, "ColorSchemeType")
        doc.attrib["ColorSchemeName"] = filename.split("/")[-1]
        xml_tree = xmltodict.parse(svg.read())
        for color in xml_tree["svg"]["g"][1]["rect"]:
            fill = dict(
                [
                    entry.split(":")
                    for entry in [entry for entry in color["@style"].split(";")]
                ]
            )["fill"]
            color_id = color["@id"]
            ET.SubElement(doc, color_id).text = fill

        tree = ET.ElementTree(root)
        tree.write(filename + ".xml")


if __name__ == "__main__":
    f = []
    for dirpath, dirnames, filenames in walk("import/"):
        f.extend(filenames)
        break

    for svg_file in f:
        if not svg_file.endswith(".svg"):
            continue
        print(svg_file)
        parse_svg("import/" + svg_file)
