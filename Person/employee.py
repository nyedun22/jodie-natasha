from person import Person


class Employee(Person):

    # constructor using key instance variables from person class
    def __init__(self, first, last, salary, num_of_sales):
        super().__init__(first, last)
        # additional instance variables
        self.salary = salary
        self.num_of_sales = num_of_sales
        self.revenue = self.num_of_sales * Person.item_cost
        self.commission_amount = self.revenue * Person.commission_amount

    # change email to company email address from default gmail
    @property
    def email(self):
        return f'{self.first}{self.last}@company.com'.lower()

    # method to calculate commission based on num of total sales
    # return total salary (salary + commission)
    def apply_commission(self):
        if self.num_of_sales >= 100:
            Person.commission_amount = 1.10
            return self.salary + self.commission_amount
        else:
            return self.salary + self.commission_amount

    def __str__(self):
        return f' Employee name: {self.fullname} \n Contact details: {self.email} \n Salary: £{self.salary} \n Commission: £{self.commission_amount}'


employee_1 = Employee('Sarah', 'Jenkins', 30000, 70)
employee_2 = Employee('James', 'Evans', 30000, 101)
print(employee_1)
print(employee_1.apply_commission())

print(employee_2)
print(employee_2.apply_commission())
