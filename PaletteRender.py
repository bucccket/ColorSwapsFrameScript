import os
from PIL import Image, ImageDraw, ImageColor, ImageFont


class PaletteRenderer:
    fnt_header = ImageFont.truetype("arial.ttf", 52, encoding="unic")
    fnt_body = ImageFont.truetype("arial.ttf", 28, encoding="unic")
    img_size = 500
    rect_size = 50  # px
    margin = 7  # px

    def __init__(self, xml_dict):
        self.img = Image.new(
            "RGB", (self.img_size, self.img_size), color=ImageColor.getrgb("#9b9b9b")
        )
        self.context = ImageDraw.Draw(self.img, "RGBA")
        self.xml_dict = xml_dict
        self.title = self.xml_dict["@ColorSchemeName"]

    def Render(self, name="img/output.png"):
        self.__RenderTitle()
        self.__RenderText()
        self.__RenderTiles()
        self.SaveAs(name)

    def __RenderTitle(self):
        x, y = (10, 10)

        color = self.__GetKey("IndicatorColor")

        # thin border
        self.context.text((x - 2, y), self.title, font=self.fnt_header, fill=(0, 0, 0, 255))
        self.context.text((x + 2, y), self.title, font=self.fnt_header, fill=(0, 0, 0, 255))
        self.context.text((x, y - 2), self.title, font=self.fnt_header, fill=(0, 0, 0, 255))
        self.context.text((x, y + 2), self.title, font=self.fnt_header, fill=(0, 0, 0, 255))

        self.context.text((x, y), self.title, font=self.fnt_header, fill=color)

    def __RenderText(self):
        offsetX = 10
        offsetY = 90

        names = ["Hair", "Body", "Body2", "Special", "Cloth", "Weapon", "Indicator"]

        for idx in range(0, len(names)):
            px = offsetX
            py = idx * (self.rect_size + self.margin) + offsetY
            self.context.text(
                (px, py), names[idx], font=self.fnt_body, fill=(0, 0, 0, 255)
            )

    def __RenderTiles(self):
        offsetX = 150
        offsetY = 90

        colorMap = self.__GetColorMap()

        for y in range(0, 7):
            for x in range(0, 6):
                color = colorMap[y][x]
                inverted = (255 - color[0], 255 - color[1], 255 - color[2], 255)

                if color == (0, 0, 0, 255):
                    continue

                px = x * (self.rect_size + self.margin) + offsetX
                py = y * (self.rect_size + self.margin) + offsetY

                self.context.rectangle(
                    [(px, py), (px + self.rect_size, py + self.rect_size)],
                    fill=color,
                    outline=inverted,
                    width=1,
                )

    def __GetColorMap(self):
        # due to shallow lists
        # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
        colors = [[(0, 0, 0, 255) for x in range(6)] for y in range(7)]

        colors[0][1] = self.__GetKey("HairLt_Swap")
        colors[0][2] = self.__GetKey("Hair_Swap")
        colors[0][3] = self.__GetKey("HairDk_Swap")

        colors[1][0] = self.__GetKey("Body1VL_Swap")
        colors[1][1] = self.__GetKey("Body1Lt_Swap")
        colors[1][2] = self.__GetKey("Body1_Swap")
        colors[1][3] = self.__GetKey("Body1Dk_Swap")
        colors[1][4] = self.__GetKey("Body1VD_Swap")
        colors[1][5] = self.__GetKey("Body1Acc_Swap")

        colors[2][0] = self.__GetKey("Body2VL_Swap")
        colors[2][1] = self.__GetKey("Body2Lt_Swap")
        colors[2][2] = self.__GetKey("Body2_Swap")
        colors[2][3] = self.__GetKey("Body2Dk_Swap")
        colors[2][4] = self.__GetKey("Body2VD_Swap")
        colors[2][5] = self.__GetKey("Body2Acc_Swap")

        colors[3][0] = self.__GetKey("SpecialVL_Swap")
        colors[3][1] = self.__GetKey("SpecialLt_Swap")
        colors[3][2] = self.__GetKey("Special_Swap")
        colors[3][3] = self.__GetKey("SpecialDk_Swap")
        colors[3][4] = self.__GetKey("SpecialVD_Swap")
        colors[3][5] = self.__GetKey("SpecialAcc_Swap")

        colors[4][0] = self.__GetKey("ClothVL_Swap")
        colors[4][1] = self.__GetKey("ClothLt_Swap")
        colors[4][2] = self.__GetKey("Cloth_Swap")
        colors[4][3] = self.__GetKey("ClothDk_Swap")

        colors[5][0] = self.__GetKey("WeaponVL_Swap")
        colors[5][1] = self.__GetKey("WeaponLt_Swap")
        colors[5][2] = self.__GetKey("Weapon_Swap")
        colors[5][3] = self.__GetKey("WeaponDk_Swap")
        colors[5][5] = self.__GetKey("WeaponAcc_Swap")

        colors[6][0] = self.__GetKey("IndicatorColor")

        return colors

    def __GetKey(self, key):
        val = "000000"
        try:
            val = self.xml_dict[key]
            val = val.removeprefix("#")
            val = val.removeprefix("0x")
            val = val.removeprefix("0X")
        except Exception as e:
            print('Failed Getting Key "{0}" for {1}'.format(key,self.title))

        num = 0
        try:
            barr = bytearray.fromhex(val)
            num = int.from_bytes(barr, byteorder="big", signed=False)
        except Exception as e:
            print('Failed Decoding Color "{0}" for "{1}"'.format(val, self.title))
            print(e)

        return ((num >> 16) & 0xFF, (num >> 8) & 0xFF, num & 0xFF, 255)  # R G B

    def SaveAs(self, filename):
        export_path = os.path.dirname(filename)
        if not os.path.exists(export_path):
            try:
                os.makedirs(export_path)
            except Exception as e:
                print("Failed Creating Export Directory")
                print(e)
                return
        self.img.save(filename)

    def Save(self):
        self.SaveAs("img/output.png")
