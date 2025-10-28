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
        self.__tempo_uso = 0

    def set_battery(self, bateria: Bateria):
        self.__bateria = bateria

    def set_charger(self, carregador: Carregador):
        if self.__carregador is not None:
            print("fail: carregador já conectado")
            return

        self.__carregador = carregador

    def turn_on(self):
        if self.__ligado:
            print("fail: notebook ja esta ligado")
            return
        if not self.__bateria and not self.__carregador:
            print("fail: não foi possível ligar")
            return
        if self.__bateria and self.__bateria.getCharge() > 0 or self.__carregador:
            self.__ligado = True
            self.__tempo_uso = 0
        else:
            print("fail: sem carga na bateria e sem carregador")

    def turn_off(self):
        if not self.__ligado:
            print("fail: notebook já está desligado")
        else:
            self.__ligado = False

    def remove_charger(self):
        if self.__carregador is None:
            print("fail: Sem carregador")
            return
        print(f"Removido {self.__carregador.getPotencia()}W")
        self.__carregador = None
        if self.__ligado:
            if not self.__bateria or (self.__bateria and self.__bateria.getCharge() <= 0):
                self.__ligado = False

    def remove_battery(self):
        if self.__bateria is None:
            print("fail: Sem bateria")
            return
        print(f"Removido {self.__bateria}")
        self.__bateria = None
        if self.__ligado and self.__carregador is None:
            self.__ligado = False

    def use(self, tempo: int):
        if not self.__ligado:
            print("fail: desligado")
            return
        if not self.__bateria:
            self.__tempo_uso += tempo
            return
        for i in range(tempo):
            if self.__carregador:
                self.__bateria.carregar(self.__carregador.getPotencia())
            else:
                self.__bateria.descarregar(1)
            if self.__bateria.getCharge() <= 0 and not self.__carregador:
                print("fail: descarregou")
                self.__ligado = False
                self.__tempo_uso += (i + 1)
                return

        self.__tempo_uso += tempo

    def show(self):
        estado = "ligado" if self.__ligado else "desligado"
        saida = f"Notebook: {estado}"

        if self.__ligado:
            saida += f" por {self.__tempo_uso} min"
        if self.__carregador:
            saida += f", Carregador {self.__carregador.getPotencia()}W"
        if self.__bateria:
            saida += f", Bateria {self.__bateria}"

        print(saida)


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
            nb.show()

        elif cmd == "set_battery":
            carga = int(args[1])
            cap = carga
            if len(args) > 2:
                cap = int(args[2])

            nb.set_battery(Bateria(carga, cap))

        elif cmd == "set_charger":
            pot = int(args[1])
            nb.set_charger(Carregador(pot))

        elif cmd == "turn_on":
            nb.turn_on()

        elif cmd == "turn_off":
            nb.turn_off()

        elif cmd == "use":
            tempo = int(args[1])
            nb.use(tempo)

        elif cmd == "rm_charger":
            nb.remove_charger()

        elif cmd == "rm_battery":
            nb.remove_battery()

        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
