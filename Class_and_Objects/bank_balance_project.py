
""" Create a bank account application that has balance, method of withdrawal, deposit method,
display balance on the screen. Create an instance of the bank account and ensure the methods work well.
 """

class BankAccount(object):
    """" Class variable to check account balance"""
    
    def __init__(self, balance = 0.0):
        self.balance = balance

    def display_balance(self):
        print(f"Your Balance is {self.balance}. ")

    def make_deposit(self):
        amount = float(input("How much would you love to deposit: >>> "))
        self.balance += amount
        print(f'Balance is now {self.balance}.')

    def make_withdrawal(self):
        amount = float(input("How much do you want to withdraw today? >>> "))
        if amount > self.balance:
            print(f"You have insufficient funds, your balance is {self.balance}. ")
        else:
            self.balance -= amount
            print(f"Withdrawal successful: balance is not {self.balance}. ")
    
mybank = BankAccount(20000)
mybank.display_balance()
mybank.make_deposit()
mybank.make_withdrawal()
