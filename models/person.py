class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age == self._age + 1:
            self._age = new_age
        else:
            raise ValueError('You can only increment the age by 1')

    def __str__(self) -> str:
        return f'{self.name} is {self._age} years old.'
