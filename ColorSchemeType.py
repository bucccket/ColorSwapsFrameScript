from PCode import PCode


class ColorSchemeType:
    
    def __init__(self, xml_dict):
        self.xml_dict = xml_dict
        self.name = self.xml_dict["@ColorSchemeName"]
        self.colors = [0] * 35
        self.__ParseXmlDict()
        
    def __GetKey(self, key):
        val = "000000"
        try: 
            val = self.xml_dict[key]
            val = val.removeprefix("#")
            val = val.removeprefix("0x")
            val = val.removeprefix("0X")
        except Exception as e:
            print('Failed Getting Key "{0}" for "{1}"'.format(key, self.name))
        return self.__DecodeColor(val)

    def __DecodeColor(self, color):
        num = 0
        try:
            barr = bytearray.fromhex(color)
            num = int.from_bytes(barr, byteorder="big", signed=False)
        except Exception as e:
            print('Failed Decoding Color "{0}" for "{1}"'.format(color, self.name))
            print(e)
        return num

    def __ParseXmlDict(self):
        
        # unused magical 0th swap??
        self.colors[1] = self.__GetKey("HairLt_Swap")
        self.colors[2] = self.__GetKey("Hair_Swap")
        self.colors[3] = self.__GetKey("HairDk_Swap")
        self.colors[4] = self.__GetKey("Body1VL_Swap")
        self.colors[5] = self.__GetKey("Body1Lt_Swap")
        self.colors[6] = self.__GetKey("Body1_Swap")
        self.colors[7] = self.__GetKey("Body1Dk_Swap")
        self.colors[8] = self.__GetKey("Body1VD_Swap")
        self.colors[9] = self.__GetKey("Body1Acc_Swap")
        self.colors[10] = self.__GetKey("Body2VL_Swap")
        self.colors[11] = self.__GetKey("Body2Lt_Swap")
        self.colors[12] = self.__GetKey("Body2_Swap")
        self.colors[13] = self.__GetKey("Body2Dk_Swap")
        self.colors[14] = self.__GetKey("Body2VD_Swap")
        self.colors[15] = self.__GetKey("Body2Acc_Swap")
        self.colors[16] = self.__GetKey("SpecialVL_Swap")
        self.colors[17] = self.__GetKey("SpecialLt_Swap")
        self.colors[18] = self.__GetKey("Special_Swap")
        self.colors[19] = self.__GetKey("SpecialDk_Swap")
        self.colors[20] = self.__GetKey("SpecialVD_Swap")
        self.colors[21] = self.__GetKey("SpecialAcc_Swap")
        # unused skin swaps 22-25
        self.colors[26] = self.__GetKey("ClothVL_Swap")
        self.colors[27] = self.__GetKey("ClothLt_Swap")
        self.colors[28] = self.__GetKey("Cloth_Swap")
        self.colors[29] = self.__GetKey("ClothDk_Swap")
        self.colors[30] = self.__GetKey("WeaponVL_Swap")
        self.colors[31] = self.__GetKey("WeaponLt_Swap")
        self.colors[32] = self.__GetKey("Weapon_Swap")
        self.colors[33] = self.__GetKey("WeaponDk_Swap")
        self.colors[34] = self.__GetKey("WeaponAcc_Swap")

    def ExportToPCode(self, PClass, PVector, PArray):
        pcode = PCode(PClass, PVector, PArray)
        return pcode.Generate(self.colors)

    pass
