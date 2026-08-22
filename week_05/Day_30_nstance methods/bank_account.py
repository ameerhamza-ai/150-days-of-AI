class BankAccount:
    def __init__(self, owner, account_no, balance=0):
        self.owner = owner
        self.account_no = account_no
        # Private attributes using double underscore (__)
        self.__balance = balance
        self.__transactions = []

        if balance > 0:
            self.__transactions.append(f"Initial deposit: Rs.{balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposited: +Rs.{amount}")
            print(f"Rs.{amount} deposited to {self.owner}'s account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Withdrawn: -Rs.{amount}")
            print(f"Rs.{amount} withdrawn by {self.owner}.")
        else:
            print(f"Withdrawal failed. Insufficient funds or invalid amount.")

    def transfer(self, amount, other_account):
        # We withdraw from 'self' and deposit to 'other_account'
        if 0 < amount <= self.__balance:
            self.withdraw(amount)
            # Use public method to deposit into the other account
            other_account.deposit(amount)
            self.__transactions.append(f"Transferred: Rs.{amount} to Acc {other_account.account_no}")
            print(f"Transfer of Rs.{amount} successful.")
        else:
            print("Transfer failed. Check balance.")

    def check_balance(self):
        print(f"Balance for {self.owner}: Rs.{self.__balance}")
        return self.__balance

    def get_statement(self):
        print(f"\n--- Statement for {self.owner} (Acc: {self.account_no}) ---")
        for t in self.__transactions:
            print(t)
            print("---------------------------------------")

    def __str__(self):
        return f"Account({self.account_no}) | Owner: {self.owner} | Balance: Rs.{self.__balance}"

# --- TESTING ---
acc1 = BankAccount("Ameer Hamza", "PK123", 5000)
acc2 = BankAccount("Ali", "PK999", 1000)

print(acc1)
acc1.deposit(2000)
acc1.withdraw(1500)
acc1.transfer(1000, acc2)

acc1.get_statement()
acc2.get_statement()