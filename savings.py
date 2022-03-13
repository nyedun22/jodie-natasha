from exercise16_banks import SavingAccount

rachel_account = SavingAccount(1000, 0.05)
rachel_account.deposit(300)
rachel_account.withdraw(500)


print(rachel_account)
print(rachel_account.interest_balance())
