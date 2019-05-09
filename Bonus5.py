class BankAccount:
    balance = float(500.15)


class Deposit:
    def __init__(self, deposit_amount):
        self.deposit_amount = deposit_amount
        BankAccount.balance += float(deposit_amount)
        print("Your account balance is $" + repr(BankAccount.balance))

class Withdrawal:
    def __init__(self, withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount
        BankAccount.balance -= float(withdrawal_amount)
        print("Your account balance is $" + repr(BankAccount.balance))



print("Welcome to Bank of Python")
print("You account balance is $" + repr(BankAccount.balance))

Deposit(100)
Withdrawal(50.15)


