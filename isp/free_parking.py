from abc import ABC, abstractmethod

from isp.parking_lot import ParkingLot


class FreeParking(ParkingLot):

    def __init__(self):
        self.capacity = 50
        self.hourly_fee = 0

    def car_arrives(self):
        self.capacity -= 1

    def car_leaves(self):
        self.capacity += 1

    def get_capacity(self):
        return self.capacity

    def calculate_fee(self, number_of_hours):
        return 0

    def process_payment(self, fee):
        raise NotImplementedError('No payment possible at free parking')
