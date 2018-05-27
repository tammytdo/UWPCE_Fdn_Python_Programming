"""

Assignment 08

Create a Banking program

"""

# Create a Banking class that does the following: 
class Banking:

    # Tracks an initial account balance
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # Tracks deposits in the account
    def make_deposit(self):
        user_deposit = float(input("How much do you want to deposit?: "))
        self.balance += user_deposit
        print("You deposited ${:,.2f}".format(user_deposit))
        return self.balance

    # Tracks withdrawals to the account
    def make_withdrawal(self):
        user_withdrawal = float(input("How much do you want to withdraw?: "))
        self.balance -= user_withdrawal
        print("You withdrew ${:,.2f}".format(user_withdrawal))
        return self.balance
        return user_withdrawal

    # Prints out a current balance
    def print_current_balance(self):
        user_print = input("Do you want to print your balance?: ")
        if user_print == "yes".lower():
            print("Your balance is ${:,.2f}".format(self.balance))
        elif user_print == "no".lower():
            print("You chose to not print your balance.")
        else:
            print("Unsure of your selection. Have a great day.")

    # Prints an error message if someone tries to withdraw more money than what is currently in the account
    def raise_overdraft_error(self):
        try:
            self.balance - user_withdrawal >= 0
        except Exception:
            print("Balance is now below 0. Deposit immediately to avoid fees.")
            raise ValueError

cust_tammy = Banking("Tammy", 50000)
cust_tammy.make_deposit()
cust_tammy.make_withdrawal()
cust_tammy.print_current_balance()
cust_tammy.raise_overdraft_error()

#Stretch goals:
# Create a script that imports the Banking class and instantiates two users with balances.
# Update the script to have the users withdraw from their bank account
# Update the script to have the users deposit to their account
# Print the user's balance.

