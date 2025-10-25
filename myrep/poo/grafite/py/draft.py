class Lead:
    def __init__(self, size: float):
        self.__size: float = size

    def size(self) -> float:
        return self.size

    def __str__(self) -> str:
        return f"Grafite: {self.size}mm"


class Pencil:
    def __init__(self):
        