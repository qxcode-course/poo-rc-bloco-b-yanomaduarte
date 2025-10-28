class Watch:
    def __init__(self, hour: int, minutes: int, seconds: int) -> None:
        self.setHour(hour)
        self.setMinutes(minutes)
        self.setSeconds(seconds)

    def __str__(self) -> str:
        return f"{self.__hour:02d}:{self.__minutes:02d}:{self.__seconds:02d}"

    def getHour(self) -> int:
        return self.__hour

    def getMinutes(self) -> int:
        return self.__minutes

    def getSeconds(self) -> int:
        return self.__seconds

    def setHour(self, value: int) -> None:
        if value not in range(0, 24):
            print("fail: hora invalida")
        else:
            self.__hour = value

    def setMinutes(self, value: int) -> None:
        if value not in range(0, 60):
            print("fail: minuto invalido")
        else:
            self.__minutes = value

    def setSeconds(self, value: int) -> None:
        if value not in range(0, 60):
            print("fail: segundo invalido")
        else:
            self.__seconds = value

    def nextSecond(self) -> None:
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.__minutes += 1
        elif self.__minutes == 60:
            self.__minutes = 0
            self.__hour += 1
        elif self.__hour == 60:
            self.__hour = 0
