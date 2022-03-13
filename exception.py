from exercise16_banks import SavingAccount

bill_account = SavingAccount(2000, 0.05)
bill_account.deposit(300)
bill_account.withdraw(3000)


class InsufficientFundsException(Exception, SavingAccount):
    def __init__(self, message):
        self.message = message

    try:
        bill_account.withdraw(3000)
        if bill_account.withdraw() > bill_account.getbalance():
            raise InsufficientFundsException
    except Exception:
            print("sorry you have insufficient funds")
    # else:
    #     pass
    # finally:
    #     pass


# print(bill_account)
# print(bill_account.interest_balance())
