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

    def insert(self, lead: Lead) -> bool:
        if self.tip is None:
            self.tip = lead
            return True
        return False

    def remove(self) -> Lead | None:
        if self.tip is None:
            return None
        removed = self.tip
        self.tip = None
        return removed

    def toString(self) -> str:
        if self.tip is None:
            return "Lapiseira: sem grafite"
        return f"Lapiseira: grafite {self.tip.size}mm"

    def __str__(self) -> str:
        return self.toString()
         