from abc import ABC, abstractmethod

from isp.parking_lot import ParkingLot


class PaidParking(ParkingLot):

    def __init__(self):
        self.capacity = 150
        self.hourly_fee = 10

    def car_arrives(self):
        self.capacity -= 1

    def car_leaves(self):
        self.capacity += 1

    def get_capacity(self):
        return self.capacity

    def calculate_fee(self, number_of_hours):
        return number_of_hours * self.hourly_fee

    def process_payment(self, fee):
        # Process payment
        pass
