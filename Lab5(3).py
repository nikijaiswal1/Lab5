class BankAccount:
    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Account Holder:", self.holder, "| Account No:", self.number, "| Balance:", self.balance)

acc = BankAccount("Anita", "AC98765", 2000)
acc.show_balance()
acc.deposit(1200)
acc.show_balance()
acc.withdraw(500)
acc.show_balance()
acc.withdraw(5000)
acc.show_balance()
