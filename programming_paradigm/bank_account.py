class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance"""

        self.__account_balance = initial_balance


    def deposit(self, amount):
            """Deposit a specified amount into the account"""

            if amount > 0:
                self.__account_balance += amount
            else:
                print("Deposit must be positive.")

    def withdraw(self, amount):
            """Withdraw a specified amount if sufficient funds exist."""

            if amount > 0:
                if amount <= self.__account_balance:
                    self.__account_balance -= amount
                    return True
                else:
                    return False
            else:
                print("Withdrawal must be positive.")
                return False
        

        def display_balance(self):
             """Display the current balance."""
             print(f"Current Balance: ${self.__account_balance:.2f}")

