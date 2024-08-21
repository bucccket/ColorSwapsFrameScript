import xmltodict
import xml.etree.cElementTree as ET

full_filename = "SvgTemplate.svg"

assert full_filename.endswith(".svg"), "File must be an SVG file"

with open(full_filename, "r") as svg:
    filename = full_filename[:-4]
    root = ET.Element("ColorSchemeTypes")
    doc = ET.SubElement(root, "ColorSchemeType")
    doc.attrib["ColorSchemeName"] = filename
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
