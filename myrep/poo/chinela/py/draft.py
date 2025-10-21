class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        tamanho = valor
        valor = int(input("Digite seu tamanho de chinela: "))
        if valor < 20 or valor > 50:
            print("Tamanho inválido. Digite um tamanho entre 20 e 50.")
            self.__valor = 0
            return False

        if valor % 2 != 0:
            print("Tamanho inválido. Digite um tamanho par entre 20 e 50.")
            self.__valor = 0
            return False

        self.__valor = valor
        
        return True

chinela = Chinela()


def main():
    chinela = Chinela()
    chinela.setTamanho(valor)
    print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())

if __name__ == '__main__':
    main()