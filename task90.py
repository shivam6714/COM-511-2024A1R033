"""Create a Bank Account class that stores an account holders name and balance.
   Add instance methods to deposit money, withdraw money, and display the balance.
   Donot allow a withdrawal greater than the avialble balance
"""

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        if amt>0:
            self.balance+=amt
            print(f"Deposited amount {amt} : New Balance {self.balance}")
        else:
            print(f"Amount cannot be less than or equal to ZERO")

    def withdraw(self,amt):
        if amt>self.balance:
            print(f"Insufficient Balance")
        else:
            self.balance-=amt
            print(f"Withdraw {amt} : Remaining Balance {self.balance}")

    def display(self):
        print(f"Account Holder : {self.name}")
        print(f"Account Balance : {self.balance}")

acc= BankAccount("hi",8008)
acc.display()
acc.deposit(300)
acc.withdraw(7000)
acc.withdraw(550)
acc.display()
