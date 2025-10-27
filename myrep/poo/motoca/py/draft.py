class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name: str = name
        self.__age: int = age

    def getAge(self) -> int:
        return self.__age

    def getName(self) -> str:
        return self.__name

    def toString(self) -> str:
        return f"{self.__name}:{self.__age}"


class Motoca:
    def __init__(self):
        self.__potencia: int = 1
        self.__time: int = 0
        self.__pessoa: Pessoa = None

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True

    def toString(self) -> str:
        pessoa_str = "empty" if self.__pessoa is None else self.__pessoa.toString()
        return f"power:{self.__potencia}, time:{self.__time}, person:({pessoa_str})"

    def remover(self) -> 'Pessoa | None':
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return None

        pessoa_removida = self.__pessoa
        self.__pessoa = None
        return pessoa_removida

    def buyTime(self, time: int) -> None:
        self.__time += time

    def drive(self, time: int) -> None:
        if self.__time <= 0:
            print("fail: buy time first")
            return

        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return

        if self.__pessoa.getAge() > 10:
            print("fail: too old to drive")
            return

        novo_tempo = self.__time - time

        if novo_tempo <= 0:
            minutos_dirigidos = self.__time
            self.__time = 0
            print(f"fail: time finished after {minutos_dirigidos} minutes")
            return

        self.__time = novo_tempo

    def honk(self) -> str:
        return "P" + ("e" * self.__potencia) + "m"

    def init(self, potencia: int) -> None:
        self.__potencia = potencia


def main():
    moto = Motoca()

    while True:
        line = input()
        print(f"${line}")
        if line == "end":
            break

        args = line.split()
        comando = args[0]

        if comando == "show":
            print(moto.toString())

        elif comando == "init" and len(args) == 2:
            potencia_str = args[1]
            if not potencia_str.isdigit():
                print("fail: invalid power")
                continue
            moto.init(int(potencia_str))

        elif comando == "enter" and len(args) == 3:
            name = args[1]
            age_str = args[2]

            if not age_str.isdigit():
                print("fail: invalid age")
                continue

            age = int(age_str)
            pessoa = Pessoa(name, age)
            moto.inserir(pessoa)

        elif comando == "leave":
            p = moto.remover()
            if p is not None:
                print(p.toString())

        elif comando == "buy" and len(args) == 2:
            minutos = args[1]
            if not minutos.isdigit():
                print("fail: invalid time")
                continue
            moto.buyTime(int(minutos))

        elif comando == "drive" and len(args) == 2:
            minutos = args[1]
            if not minutos.isdigit():
                print("fail: invalid time")
                continue
            moto.drive(int(minutos))

        elif comando == "honk":
            print(moto.honk())

        else:
            print("fail: invalid command")


if __name__ == "__main__":
    main()

#solved