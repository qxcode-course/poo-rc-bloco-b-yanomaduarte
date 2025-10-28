class Bateria:
    def __init__(self, carga: int, capacidade: int):
        self.__carga = carga
        self.__capacidade = capacidade

    def getCharge(self):
        return self.__carga

    def getCapacity(self):
        return self.__capacidade

    def carregar(self, valor: int):
        self.__carga += valor
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def descarregar(self, valor: int):
        self.__carga -= valor
        if self.__carga < 0:
            self.__carga = 0

    def __str__(self):
        return f"{self.__carga}/{self.__capacidade}"


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria = None
        self.__carregador = None

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador

    def ligar(self):
        if self.__ligado:
            print("fail: notebook ja esta ligado")
            return
        if not self.__bateria and not self.__carregador:
            print("fail: nao ha bateria nem carregador")
            return
        if self.__bateria and self.__bateria.getCarga() >= 0:
            self.__ligado = True
            print("notebook ligado (usando bateria)")
        elif self.__carregador:
            self.__ligado = True
            print("notebook ligado (usando carregador)")
        else:
            print("fail: sem carga na bateria e sem carregador")

        def desligar(self):
            if not self.__ligado:
                print("fail: notebook já está desligado")
            else:
                self.__ligado = False
                print("notebook desligado")

        def mostrar(Self):
            estado = "ligado" if self.__ligado else "desligado"
            bat = str(self.__bateria) if self.__bateria else "sem bateria"
            car = f"{self.__carregador.getPotencia()}W" if self.__carregador else "sem carregador"
            print(f"Notebook {estado} | Bateria: {bat} | Carregador: {car}")

        def usar(self, tempo: int):
            if not self.__ligado:
                print("fail: notebook está desligado, impossivel usar")
                return
            if not self.__bateria:
                print("fail: notebook sem bateria")
                return
            for i in range(tempo):
                if self.__carregador:
                    self.__bateria.carregador(self.__carregador.getPotencia())
                else:
                    self.__bateria.descarregar(1)
                if self.__bateria.getCarga() <= 0 and not self.__carregador:
                    print("fail: bateria acabou, notebook desligando")
                    self.__ligado = False
                    break
            print("usou o notebook por {tempo} minutos")


def main():
    nb = Notebook()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()
        if len(args) == 0:
            continue

        cmd = args[0]

        if cmd == "end":
            break

        elif cmd == "show":
            nb.mostrar()

        elif cmd == "setBat":
            carga = int(args[1])
            cap = int(args[2])
            nb.setBateria(Bateria(carga, cap))

        elif cmd == "setCar":
            pot = int(args[1])
            nb.setCarregador(Carregador(pot))

        elif cmd == "ligar":
            nb.ligar()

        elif cmd == "desligar":
            nb.desligar()

        elif cmd == "usar":
            tempo = int(args[1])
            nb.usar(tempo)

        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
