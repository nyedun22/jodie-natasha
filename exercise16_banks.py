class Account:
    numCreated = 0

    def __init__(self, initial):

        self.__balance = initial
        self.semiPrivate = "hello from account"
        Account.numCreated += 1
        self.__testItem = "yes"
        self.__holder_name = ""

    def deposit(self, amt):
        self.__balance += amt
        return

    def withdraw(self, amt):
        if amt > self.__balance:
            raise InsufficientFundsException
        else:
            self.__balance -= amt
            return

    def getbalance(self):
        return self.__balance

    def get_holder_name(self):
        return self.__holder_name

    def set_holder_name(self, name):
        self.__holder_name = name
        return

    # #getter (decorator)
    # @property
    # def description(self):
    #     return self._description
    #
    # #setter
    # @description.setter
    # def description(self, description):
    #     self._description = description

    def __str__(self):
        return "Account has balance " + str(self.getbalance())

    def __add__(self, other):
        return self.getbalance() + other.getbalance()


class SavingAccount(Account):

    def __init__(self, initial, interest_rate):
        super().__init__(initial)
        self._interest_rate = interest_rate

    def __str__(self):
        savings_info = self.get_holder_name()
        savings_info += "Savings "
        savings_info += super().__str__()
        return savings_info

    def calculate_interest(self):
        return self.getbalance() * self._interest_rate

    def interest_balance(self):
        return self.getbalance() + self.calculate_interest()

bill_account = (300, 0.05)

class InsufficientFundsException(Exception):
    try:
        bill_account.withd
    except Exception:
        print("Sorry you have insufficient funds")
