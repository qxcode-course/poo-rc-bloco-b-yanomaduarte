class Lead:
    def __init__(self, size: float):
        self.__size: float = float(size)

    def __str__(self) -> str:
        return f"Grafite: {self.size}mm"


class Pencil:
    def __init__(self):
        self.tip: Lead | None = None

    def hasGrafite(self) -> bool:
        return self.tip is not None
