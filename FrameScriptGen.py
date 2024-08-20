import os

import xmltodict

from ColorSchemeType import ColorSchemeType
from PaletteRender import PaletteRenderer

ColorSwapClass = "_-E3k"
ColorSwapVector = "_-41Z"  # last static vector of ColorSwapClass
ColorSwapArray = "_-P3T"  # last non-static public Array

def main():
    xml_tree = LoadXML()
    colorschemes = GenerateColorSchemes(xml_tree)
    ExportColorSchemes(colorschemes)
    RenderColorSchemes(colorschemes)


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
    for colorscheme in xml_tree["ColorSchemeTypes"]["ColorSchemeType"]:
        colorschemes.append(ColorSchemeType(colorscheme))
    return colorschemes


def LoadXML():
    xml_tree = {}
    try:
        xml_file = open("ColorSchemeTypes.xml", "r")
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
    main()
