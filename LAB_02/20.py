from datetime import datetime
class Transaction:
    def __init__(self, trans_type, amount):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        self.type = trans_type  
        self.amount = amount

    def __str__(self):
        return f"{self.date} | {self.type:<10} | ${self.amount:.2f}"
    
class Account:
    def __init__(self, owner, pin, balance=0.0):
        self.owner = owner
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amount
        self.transactions.append(Transaction("Withdrawal", amount))
        return True

    def print_statement(self):
        print(f"\nTransaction History for {self.owner}:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print(" ", t)
        print(f"Current Balance: ${self.balance:.2f}")

class ATM:
    def __init__(self):
        self.current_account = None
        self.is_authenticated = False

    def insert_card(self, account):
        self.current_account = account
        self.is_authenticated = False
        print(f"Card inserted for {account.owner}.")

    def enter_pin(self, pin):
        if pin == self.current_account.pin:
            self.is_authenticated = True
            print("PIN accepted. You can now use ATM services.")
        else:
            print("Incorrect PIN.")

    def withdraw(self, amount):
        if not self.is_authenticated:
            print("Please enter your PIN first.")
            return
        if self.current_account.withdraw(amount):
            print(f"You withdrew ${amount:.2f}.")
        print(f"Remaining Balance: ${self.current_account.balance:.2f}")

    def deposit(self, amount):
        if not self.is_authenticated:
            print("Please enter your PIN first.")
            return
        self.current_account.deposit(amount)
        print(f"You deposited ${amount:.2f}.")
        print(f"New Balance: ${self.current_account.balance:.2f}")

    def print_statement(self):
        if not self.is_authenticated:
            print("Please enter your PIN first.")
            return
        self.current_account.print_statement()

acc1 = Account("Alice", pin="1234", balance=500.0)

atm = ATM()

atm.insert_card(acc1)
atm.enter_pin("1234")

atm.deposit(200)
atm.withdraw(100)
atm.withdraw(700)  

atm.print_statement()