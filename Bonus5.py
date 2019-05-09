class BankAccount:
    balance = 150.34


class Deposit:
    def __init__(self, deposit_amount):
        self.deposit_amount = deposit_amount
        BankAccount.balance += float(deposit_amount)
        print("Your account balance is ${:.2f}".format(BankAccount.balance))


class Withdrawal:
    def __init__(self, withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount
        BankAccount.balance -= float(withdrawal_amount)
        print("Your account balance is ${:.2f}".format(BankAccount.balance))


print("Welcome to Bank of Python")
print("Press 1 to see your account balance.")
print("Press 2 to make a deposit.")
print("Press 3 to make a withdrawal.")
action = int(input("Please make your selection now: "))

if action == 1:
    print("Your account balance is ${:.2f}".format(BankAccount.balance))
elif action == 2:
    money_amount = input("How much would you like to deposit? :")
    Deposit(money_amount)
elif action == 3:
    money_amount = input("How much would like like to withdrawal? :")
    Withdrawal(money_amount)
else:
    print("Invalid Entry.  Goodbye :)")
