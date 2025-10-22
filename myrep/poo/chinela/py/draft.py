class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        if valor < 20 or valor > 50:
            print("Tamanho inválido. Digite um tamanho entre 20 e 50.")
            return

        if valor % 2 != 0:
            print("Tamanho inválido. Digite um tamanho par entre 20 e 50.")
            return

        self.__tamanho = valor


chinela = Chinela()

while chinela.getTamanho() == 0:
    print("Digite se tamanho de chinela")
    tamanho = int(input())
    chinela.setTamanho(tamanho)

print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())
