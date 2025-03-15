import os
from os import walk

import xmltodict

from ColorSchemeType import ColorSchemeType
from PaletteRender import PaletteRenderer

ColorSwapClass =  "_-r35" # _> COLOR_BODY1_LT
ColorSwapVector = "_-J2"  # last static vector of ColorSwapClass
ColorSwapArray =  "_-s5x"  # last non-static public Array


def RenderColorSchemes(colorschemes):
    for colorscheme in colorschemes:
        render = PaletteRenderer(colorscheme.xml_dict)
        render.Render("img/" + colorscheme.name + ".png")
        render.Save()


def ExportColorSchemes(colorschemes):
    for colorscheme in colorschemes:
        data = colorscheme.ExportToPCode(
            ColorSwapClass, ColorSwapVector, ColorSwapArray
        )
        filename = "export\\" + colorscheme.name + ".pcode"

        export_path = os.path.dirname(filename)
        if not os.path.exists(export_path):
            try:
                os.makedirs(export_path)
            except Exception as e:
                print("Failed Creating Export Directory")
                print(e)
                return

        fd = open(filename, "w")
        fd.write(data)
        fd.close()


def GenerateColorSchemes(xml_tree):
    colorschemes = []
    colorschmetype = xml_tree["ColorSchemeTypes"]["ColorSchemeType"]
    if isinstance(colorschmetype, list):
        for colorscheme in xml_tree["ColorSchemeTypes"]["ColorSchemeType"]:
            colorschemes.append(ColorSchemeType(colorscheme))
    else:
        colorschemes.append(ColorSchemeType(colorschmetype))
    return colorschemes


def LoadXML(xml_file_name: str):
    xml_tree = {}
    try:
        xml_file = open(xml_file_name, "r")
    except Exception as e:
        print("Failed Opening XML File")
        print(e)
    else:
        try:
            xml_tree = xmltodict.parse(xml_file.read())
        except Exception as e:
            print("Failed Parsing XML File")
            print(e)
        xml_file.close()

    return xml_tree


if __name__ == "__main__":
    f = []
    for dirpath, dirnames, filenames in walk("import/"):
        f.extend(filenames)
        break

    for xml_file_name in f:
        if not xml_file_name.endswith(".xml"):
            continue
        xml_tree = LoadXML("import/" + xml_file_name)
        colorschemes = GenerateColorSchemes(xml_tree)
        ExportColorSchemes(colorschemes)
        RenderColorSchemes(colorschemes)
