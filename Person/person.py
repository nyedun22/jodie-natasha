# Person - parent class
class Person:
    commission_amount = 1.05
    item_cost = 10

    # constructor to pass through all key instance variables
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # decorator to access method like an attribute (this will be default value for email)
    @property
    def email(self):
        return f'{self.first}{self.last}@gmail.com'.lower()

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
