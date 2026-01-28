class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"Deposited money = {amount}.Updated Balance = {self.balance}")
    
    def withdraw(self,amount):
        if self.balance < 0:
            print("Insufficent Funds")
        elif amount > self.balance:
            print("Insufficent Funds")
        else:
            self.balance -=amount
            print(f"Withdraw {amount}. New balance = {self.balance}")

    def check_balance(self):
        print(f"Current balance:{self.balance}")
        return self.balance

account = BankAccount("Manish Kumar", 5000)
account.check_balance()
account.deposit(2000)
account.withdraw(1500)
account.check_balance()
