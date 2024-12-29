# Create a Bank class with two variables name and balance. Implement a constructor to initialize the variables. Also implement deposit and withdrawals using instance methods.

class Bank:
    def __init__(self, name, balance=0.0):
        """Constructor to initialize the name and balance of the account."""
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Method to display the current balance."""
        print(f"Account holder: {self.name}, Current balance: {self.balance}")

account = Bank("Alice", 1000.0)

# Display initial balance
account.display_balance()

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Attempt to withdraw more than the balance
account.withdraw(1500)

# Display final balance
account.display_balance()
