class account():
    def __init__ (self):
        self.owner = input("Enter your name: ")
        self.balance = 0
    def deposit(self):
        amount = int(input("Enter the amount: "))
        self.balance += amount
        if amount > 0:
            print(f"Deposit of {amount} successful. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self):
        amount = int(input("Enter the withdrawal amount: "))
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} successful. Remaining balance: ${self.balance}.")
            else:
                print("Insufficient funds for withdrawal.")
                print(f"Your balance is: {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"


myAccount = account()
print("Account creation:")
print(myAccount)
i = "0"
while i != "E":
    i = input("Enter your request D/W/E : ")
    if i == "D" :
        print("\nMaking deposits:")
        print(myAccount.deposit())
    if i == "W":
        print("\nMaking withdrawals:")
        print(myAccount.withdraw())
    else:
        pass

print("\nFinal account status:")
print(myAccount)

        