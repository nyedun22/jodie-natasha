from exercise16_banks import SavingAccount, InsufficientFundsException


try:
    rachel_account = SavingAccount(1000, 0.05)
    rachel_account.deposit(300)
    rachel_account.withdraw(2000)
except InsufficientFundsException as ex:
    print(ex)
    #creating a new variable for the exception, ex will now print message within the withdraw method
except Exception as ex:
    print(ex)
finally:
    print(rachel_account)
    print(rachel_account.interest_balance())
