class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str) -> bool:
        tamanho_valido = ["PP", "P", "M", "G", "GG", "XG"]
        if valor in tamanho_valido:
            self.__tamanho = valor
            return True
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return False

    def show(self):
        print(f"size: ({self.__tamanho})")


def main():
    roupa = Camisa()
    while True:
        line = input()
        print(f"${line}")
        if line == "end":
            break

        args = line.split()
        if args[0] == "show":
            roupa.show()
        elif args[0] == "size" and len(args) == 2:
            roupa.setTamanho(args[1])


if __name__ == "__main__":
    main()
