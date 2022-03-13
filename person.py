class Person:
    def __init__(self, first, last, gender):
        self.first = first
        self.last = last
        self.gender = gender

    def __str__(self):
        return f'Name: {self.first} {self.last}, \n '

    @property
    def email(self):
        return f'{self.first}{self.last}@gmail.com'.lower()

class Employee(Person):
    def __init__(self, first, last, gender, role):
        super().__init__(first, last, gender)
        self.role = role

    @property
    def email(self):
        return f'{self.first}{self.last}@company.com'.lower()

    def __str__(self):
        return f'{self.first} {self.last}, is a {self.role}. You can reach them at {self.email}'



class Customer(Person):
    def __init__(self, first, last, gender, item_purchased, number_of_purchases):
        super().__init__(first, last, gender)
        self.item_purchased = item_purchased
        self.number_of_purchases = int(number_of_purchases)

    def __str__(self):
        return f'{self.first} {self.last}: purchased {self.number_of_purchases} {self.item_purchased}'

Timmy = Person('Timmy', 'Jones', 'Male')
print(Timmy)
Sarah = Employee('Sarah', 'Brown', 'Female', 'Sales Associate')
print(Sarah)
Michael = Customer('Michael', 'Peters', 'Male', 'Cakes', 3)
print(Michael)