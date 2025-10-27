class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def getThickness(self) -> float:
        return self.__thickness

    def getHardness(self) -> str:
        return self.__hardness

    def getSize(self) -> int:
        return self.__size

    def setSize(self, size: int):
        self.__size = size

    def usagePerSheet(self) -> int:
        if self.__hardness == "HB":
            return 1
        elif self.__hardness == "2B":
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        return 0

    def __str__(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"


         
