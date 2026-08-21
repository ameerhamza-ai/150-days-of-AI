class BankAccount:
    def __init__(self,owner:str,balance:float=0.0) -> None:
        self.owner = owner 
        self.balance = balance 

    def deposit(self,amount) -> None:
           if amount > 0:
               self.balance += amount
               print(f"Successfully deposited {amount:,.2f} PKR.")
           else:
                print("Invalid deposit amount. Must be greater than 0.")

    def withdraw(self,amount) -> None:
        if amount <= 0:
            print("Invalid withdrawal amount. Must be greater than 0.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew {amount:,.2f} PKR.") 
        else:
             print(f"Insufficient funds! Current balance is only {self.balance:,.2f} PKR.")

    def check_balance(self) -> str:
         return f"Balance: {self.balance:,.2f} PKR"

    def __str__(self):
         return f"Account Owner: {self.owner} | Current Balance: {self.balance:,.2f} PKR"

if __name__ == "__main__":
    # --- ACCOUNT 1 ---
    print("=== Set Up Account 1 ===")
    owner_1 = input("Enter Owner Name: ")
    initial_bal_1 = float(input("Enter Initial Balance: "))

    acc1 = BankAccount(owner=owner_1, balance=initial_bal_1)
    print(f"\nAccount Created -> {acc1}")

    dep_1 = float(input("\nEnter amount to deposit into Account 1: "))
    acc1.deposit(dep_1)
    print(acc1.check_balance())

    with_1 = float(input("\nEnter amount to withdraw from Account 1: "))
    acc1.withdraw(with_1)
    print(acc1.check_balance())

    print("\n" + "=" * 45 + "\n")

    # --- ACCOUNT 2 ---
    print("=== Set Up Account 2 ===")
    owner_2 = input("Enter Owner Name: ")
    initial_bal_2 = float(input("Enter Initial Balance: "))

    acc2 = BankAccount(owner=owner_2, balance=initial_bal_2)
    print(f"\nAccount Created -> {acc2}")

    dep_2 = float(input("\nEnter amount to deposit into Account 2: "))
    acc2.deposit(dep_2)
    print(acc2.check_balance())

    with_2 = float(input("\nEnter amount to withdraw from Account 2: "))
    acc2.withdraw(with_2)
    print(acc2.check_balance())

    print("\n" + "=" * 45)
    print("=== Final Accounts Summary ===")
    print(acc1)
    print(acc2)


