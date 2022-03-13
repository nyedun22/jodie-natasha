from person import Person


class Customer(Person):

    # constructor using key instance variables from person class
    def __init__(self, first, last, num_purchases):
        super().__init__(first, last)
        # additional instance variables
        self.num_purchases = num_purchases

    # method to return cost of items
    # if customer buys 10 or more items, they receive 10% discount
    def total_cost(self):
        if self.num_purchases >= 10:
            Person.item_cost = Person.item_cost * 0.9
            return int(self.num_purchases * Person.item_cost)
        else:
            return int(self.num_purchases * Person.item_cost)

    def __str__(self):
        return f' CUSTOMER PROFILE: \n Name: {self.fullname} \n Contact details: {self.email} \n Purchased {self.num_purchases} items.'


customer_1 = Customer('Jenny', 'Lopez', 9)
customer_2 = Customer('Jack', 'Brown', 10)

print(customer_1)
print(customer_1.total_cost())

print(customer_2)
print(customer_2.total_cost())
