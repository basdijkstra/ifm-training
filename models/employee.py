from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, emp_id, first_name, last_name):
        self._emp_id = emp_id
        self._first_name = first_name
        self._last_name = last_name

    @property
    def name(self):
        return f'{self._first_name} {self._last_name}'

    @abstractmethod
    def salary(self):
        pass
