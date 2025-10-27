class Person:
    def __init__(self, name: str, money: float):
        self.__name = name
        self.__money = money

    def getName(self):
        return self.__name

    def getMoney(self):
        return self.__money

    def setMoney(self):
        self.__money = value