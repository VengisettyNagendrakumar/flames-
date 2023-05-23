class bankacc:
    def __init__(self):
        self.balance=0
        print("wlecome to withdrawl and deposit")
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
	self.balance += amount
	print("\n Amount Deposited:",amount)

    def withdraw(self):
        amt=int(input("enter amount to withdraw")
        self.balance -=amt
        print("amount withdraw is ",amt)
    def display(self):
        print(self.balance)

s=bankacc()
s.deposit()
s.withdraw()
s.display()
