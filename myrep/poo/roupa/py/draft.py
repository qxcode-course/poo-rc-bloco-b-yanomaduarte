class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        tamanho_valido = ["P", "M", "G", "GG", "XG"]
        if valor in tamanho_valido:
            self.__tamanho = valor
        else:
            print("Tamanho inválido. Use 'P', 'M', 'G', 'GG' ou 'XG'.")


roupa = Camisa()

while roupa.getTamanho() == "":
    tamanho_input = input("Digite o tamanho da camisa (P, M, G, GG, XG): ").strip().upper()
    roupa.setTamanho(tamanho_input)

print("Parabéns, você comprou uma camisa tamanho", roupa.getTamanho())
