class BankAcct:

    # Initializes an object with an individuals bank information
    def __init__(self, name, account_number, amount, interest_rate):

        self.__name = name
        self.__account_number = account_number
        self.__amount = amount
        self.__interest_rate = interest_rate

    # Adjusts a user's interest rate
    def adjust_rate(self, new_rate):

        # Prevents invalid interest rates
        if 0 < new_rate <= 100:
            self.__interest_rate = new_rate
            print(f"{self.__name}'s interest rate was adjusted to {self.__interest_rate}\n")
        else:
            print("Invalid Interest Rate\n")

    # Allows a user to withdraw money
    def withdraw(self, wd_amount):

        # Prevents invalid withdraw amounts
        if wd_amount > 0:
            if self.__amount > wd_amount:
                self.__amount -= wd_amount
                print(f"${wd_amount} was withdrawn from {self.__name}'s account\n")
            else:
                print(f"\nInsufficient Funds\n")
        else:
            print("\nInvalid Amount Withdrawn\n")

    # Allows a user to deposit money
    def deposit(self, dp_amount):

        # Prevents invalid deposit amounts
        if dp_amount >= 0:
            self.__amount += dp_amount
            print(f"${dp_amount} was deposited into {self.__name}'s account\n")
        else:
            print(f"\nInvalid Amount Deposited. Try Withdrawing\n")

    # Displays the user's balance
    def get_balance(self):
        return f"{self.__name}'s balance is {self.__amount:,.2f}\n"

    # Finds the interest amount for a select number of days
    def interest(self, days):
        return (f"{self.__name}'s interest for {days} days is:" +
        f" {(self.__amount * self.__interest_rate) * days:,.2f}")

    # Displays a users information
    def __str__(self):
        s = str(f"\t\t{self.__name}\n{"--" * 10}"
                f"\nAccount Number: {self.__account_number}"
                f"\nBalance: {self.__amount:,.2f}"
                f"\nInterest Rate: {self.__interest_rate}\n")
        return s

def test():

    # Creates two BankAcct instances
    acct1 = BankAcct("Tyler", "BA230", 2018.98, 0.006)
    acct2 = BankAcct("James", "BA667", 1567.3333, 0.004)

    # Displays the accounts information
    print(acct1)
    print(acct2)

    # Deposits money into acct1
    acct1.deposit(1068.53)

    # Withdraws money from acct2
    acct2.withdraw(670)

    # Gets the balance of acct2
    print(acct2.get_balance())

    # Adjusts the interest rate of acct1
    acct1.adjust_rate(0.01)

    # Displays the interest amount for acct1
    print(acct1.interest(5) + "\n")

    # Displays both accounts information
    print(acct1)
    print(acct2)



if __name__ == "__main__":
    test()