from abc import ABC, abstractmethod

class Mammals(ABC):
    @staticmethod
    @abstractmethod
    def swim():
        print("can swim")

    @staticmethod
    @abstractmethod
    def walk():
        print("can walk")

class Human(Mammals):
    @staticmethod
    def swim():
        return print("Humans can swim")

    @staticmethod
    def walk():
        return print("Humans can walk")

class Whale(Mammals):
    @staticmethod
    def swim():
        return print("Whales can swim")


Human.walk()
Human.swim()

Whale.walk()
Whale.swim()