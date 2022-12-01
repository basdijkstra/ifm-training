from abc import ABC, abstractmethod
import time


interestRate = 0.05

class Account(ABC):
    @abstractmethod
    def Withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

class SavingsAccount(Account):


    def __init__(self):
        self.balance = 0

    def Withdraw(self, amount):
        self.balance = self.balance - amount

    def calculateinterest(self):
        self.balance *= (1 + interestRate)


class checkingaccount(Account):

    def __init__(self):
        self.balance = 0

    def Withdraw(self, amount):
        self.balance -= amount