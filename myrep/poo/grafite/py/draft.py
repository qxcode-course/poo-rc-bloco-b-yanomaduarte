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


class Pencil:
    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__tip = None

    def hasGrafite(self) -> bool:
        return self.__tip is not None

    def insert(self, lead: Lead):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return

        if lead.getThickness() != self.__thickness:
            print("fail: calibre incompativel")
            return

        self.__tip = lead

    def remove(self) -> Lead:
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return

        removed_lead = self.__tip
        self.__tip = None
        return removed_lead

    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return

        if self.__tip.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return

        usage = self.__tip.usagePerSheet()
        final_size = self.__tip.getSize() - usage

        if final_size < 10:
            self.__tip.setSize(10)
            print("fail: folha incompleta")

        else:
            self.__tip.setSize(final_size)

    def __str__(self) -> str:
        tip_str = str(self.__tip) if self.hasGrafite() else "null"
        return f"calibre: {self.__thickness}, grafite: {tip_str}"


def main():
    pencil = None

    while True:
        line = input()
        print(f"${line}")
        if line == "end":
            break

        args = line.split()

        if not args:
            print("fail: comando invalido")
            continue

        command = args[0]

        if command == "init":
            if len(args) < 2:
                print("fail: argumentos insuficientes para 'init'")
                continue

            pencil = Pencil(float(args[1]))

        elif command == "show":
            if pencil:
                print(pencil)
            else:
                print("fail: lapiseira nao iniciada")

        elif pencil is None:
            print("fail: lapiseira nao iniciada")
            continue

        elif command == "insert":
            if len(args) < 4:
                print("fail: argumentos insuficientes para 'insert'")
                continue

            caliber = float(args[1])
            hardness = args[2]
            size = int(args[3])
            graphite = Lead(caliber, hardness, size)
            pencil.insert(graphite)

        elif command == "remove":
            pencil.remove()

        elif command == "write":
            pencil.writePage()

        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
