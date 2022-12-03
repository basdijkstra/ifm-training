from abc import ABC, abstractmethod

class ParkingLot(ABC):

    @abstractmethod
    def car_arrives(self):
        pass

    @abstractmethod
    def car_leaves(self):
        pass

    @abstractmethod
    def get_capacity(self):
        pass

    @abstractmethod
    def calculate_fee(self, number_of_hours):
        pass

    @abstractmethod
    def process_payment(self, fee):
        pass
