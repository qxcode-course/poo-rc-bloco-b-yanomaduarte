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

    def __str__(self):
        return f"{self.__name}:{int(self.__money)}"

class Motorcycle:
    def __init__(self):
        self.__cost = 0
        self.__driver = None
        self.__passenger = None

    def setDriver(self, person: Person):
        self.__driver = person

    def setPassenger(self, person: Person):
        self.__passenger = person

    def drive(self, km: int):
        if not self.__driver:
            print("fail: não há motorista")
            return

        if not self.__passenger:
            print("fail: não há passageiro")

        self.__cost = km

    def leavePass(self):
        if not self.__passenger:
            print("fail: não há passageiro pra sair")
            return

        run_price = self.__cost
        passenger = self.__passenger
        driver = self.__driver

        if passenger.getMoney() >= run_price:
            passenger.setMoney(passenger.getMoney() - run_price)
            driver.setMoney(driver.getMoney() + run_price)
        
        else:driver.setMoney(driver.getMoney() + run_price)
        passenger.setMoney(0)

        print(f"{passenger.getName()}:{int(passenger.getMoney())} left")

        self.__passenger = None
        self.__cost = 0

        def show(self):
            driver = str(self.__driver) if self.__driver else "None"
            passenger = str(self.__passenger) if self.__passenger else "None"


def main():
    motorcycle = Motorcycle()