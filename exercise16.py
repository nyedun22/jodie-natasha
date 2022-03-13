#create class for person, employee, and customer, use inheritance

class Person:
    def __init__(self, first, last, gender):
        self.first = first
        self.last = last
        self.gender = gender


    def __str__(self):
        return f"Name: {self.first} {self.last},\n Gender: {self.gender},\n Email: {self.email}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com".lower()


class Employee(Person):
    def __init__(self, first, last, gender, role):
        super().__init__(first, last, gender)
        self.role = role

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com".lower()

    def __str__(self):
        return f"{self.first} {self.last} is a {self.role}, you can reach them at {self.email}."


class Customer(Person):
    def __init__(self, first, last, gender, item_purchased, number_of_purchases):
        super().__init__(first, last, gender)
        self.item_purchased = item_purchased
        self.number_of_purchases = int(number_of_purchases)

    def __str__(self):
        return f"{self.first} {self.last} purchased {self.number_of_purchases} {self.item_purchased}."


timmy = Person('Timmy', 'Jones', 'male')
print(timmy)
print(timmy.email)

sarah = Employee('Sarah', 'Brown', 'female', 'Sales Associate')
print(sarah)

micheal = Customer('Micheal', 'Peters', 'male', 'cakes', 3)
print(micheal)
print(micheal.email)
