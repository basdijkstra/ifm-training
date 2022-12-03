from abc import ABC, abstractmethod

class Swimmer(ABC):
    @staticmethod
    @abstractmethod
    def swim():
        print("can swim")

class Walker(ABC):
    @staticmethod
    @abstractmethod
    def walk():
        print("can walk")

class Human(Walker, Swimmer):
    @staticmethod
    def swim():
        return print("Humans can swim")

    @staticmethod
    def walk():
        return print("Humans can walk")

class Whale(Swimmer):
    @staticmethod
    def swim():
        return print("Whales can swim")


Human.walk()
Human.swim()

Whale.swim()
Whale.walk()
