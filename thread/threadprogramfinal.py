import threading
import time

'''
print("________________________without thread_____________________________")
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        new_balance = self.balance + amount
        # Simulate a delay
        time.sleep(1)
        self.balance = new_balance
        print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            # Simulate a delay
            time.sleep(1)
            self.balance = new_balance
            print(f"Withdrew {amount}, new balance is {self.balance}")
        else:
            print(f"Insufficient funds for withdrawal of {amount}, current balance is {self.balance}")

# Function to perform deposits
def perform_deposits(account, amounts):
    for amount in amounts:
        account.deposit(amount)

# Function to perform withdrawals
def perform_withdrawals(account, amounts):
    for amount in amounts:
        account.withdraw(amount)

# Create a bank account instance
account = BankAccount()

# Define deposit and withdrawal amounts
deposit_amounts = [100, 200, 300, 400, 500]
withdrawal_amounts = [150, 250, 350, 450, 550]

# Measure the start time
start_time = time.time()

# Perform deposits sequentially
perform_deposits(account, deposit_amounts)

# Perform withdrawals sequentially
perform_withdrawals(account, withdrawal_amounts)

# Measure the end time
end_time = time.time()

# Calculate the duration
duration = end_time - start_time
print(f"All transactions completed in {duration:.2f} seconds.")

'''
print("________________________with thread_____________________________")

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            new_balance = self.balance + amount
            # Simulate a delay
            time.sleep(1)
            self.balance = new_balance
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                # Simulate a delay
                time.sleep(1)
                self.balance = new_balance
                print(f"Withdrew {amount}, new balance is {self.balance}")
            else:
                print(f"Insufficient funds for withdrawal of {amount}, current balance is {self.balance}")

# Function to perform deposits
def perform_deposits(account, amounts):
    for amount in amounts:
        account.deposit(amount)

# Function to perform withdrawals
def perform_withdrawals(account, amounts):
    for amount in amounts:
        account.withdraw(amount)

# Create a bank account instance
account = BankAccount()

# Define deposit and withdrawal amounts
deposit_amounts = [100, 200, 300, 400, 500]
withdrawal_amounts = [150, 250, 350, 450, 550]

# Create threads for deposits and withdrawals
deposit_thread = threading.Thread(target=perform_deposits, args=(account, deposit_amounts))
withdrawal_thread = threading.Thread(target=perform_withdrawals, args=(account, withdrawal_amounts))

# Measure the start time
start_time = time.time()

# Start the threads
deposit_thread.start()
withdrawal_thread.start()

# Wait for both threads to complete
deposit_thread.join()
withdrawal_thread.join()

# Measure the end time
end_time = time.time()

# Calculate the duration
duration = end_time - start_time
print(f"All transactions completed in {duration:.2f} seconds.")


