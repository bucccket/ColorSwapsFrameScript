class PCode:
    ClassName = "_-ABC"
    CstVector = "_-ABC"
    U32Array = "_-ABC"

    def __init__(self, ClassName, CstVector, U32Array):
        self.ClassName = ClassName
        self.CstVector = CstVector
        self.U32Array = U32Array

    def __GenerateHeader(self):
        return f"""
method
    name null
    returns null

    body
        maxstack 37
        localcount 14
        initscopedepth 10
        maxscopedepth 11

        code
            getlocal0
            pushscope
            getlocal0
            constructsuper 0
            pushstring "{self.ClassName}"
            coerce_s
            setlocal 6
            getlex QName(PackageNamespace("flash.system"),"ApplicationDomain")
            getproperty QName(PackageNamespace("","4"),"currentDomain")
            coerce QName(PackageNamespace("flash.system"),"ApplicationDomain")
            setlocal 4
            getlocal 4
            getlocal 6
            callproperty QName(PackageNamespace("","4"),"hasDefinition"), 1
            iffalse InvalidClass
            getlocal 4
            getlocal 6
            callproperty QName(PackageNamespace("","4"),"getDefinition"), 1
            setlocal 5
            getlocal 5
            getproperty QName(PackageNamespace("","4"),"{self.CstVector}")
            pushbyte 1
            getproperty MultinameL([PackageNamespace("","3")])
            coerce QName(PackageNamespace("","4"),"{self.ClassName}")
            setlocal 13
        """
            
    def __GenerateTable(self, colors):
        if(len(colors) != 35):
            print("Invalid number of colors. target is 35, got " + str(len(colors)))
            return
        
        code = "getlocal 13"
        for color in colors:
            code += f"""\n            pushuint {color}"""
        code += f"""
            newarray 35
            coerce QName(PackageNamespace("","4"),"Array")
            initproperty QName(PackageNamespace("","4"),"{self.U32Array}")
        """
        return code
            
    def __GenerateFooter(self):
        return """
InvalidClass:
            returnvoid
        end ; code
    end ; body
end ; method"""

    def Generate(self, colors):
        pcode = ""
        pcode += self.__GenerateHeader()
        pcode += self.__GenerateTable(colors)
        pcode += self.__GenerateFooter()
        return pcode
