# make subclasses for ATM and Account
# make a login function for ATM
# make a deposit and withdraw function for ATM
# make a function to display account details for Account
# make it so that there are saving subclasses which you can view
# streamlit app.py
# requirements.txt




class Account:
    NoOfAccounts = 0
    def __init__(self, AccName, AccNo, starting_Balance):
        self.AccName = AccName
        self.AccNo = AccNo
        self.starting_Balance = starting_Balance
        Account.NoOfAccounts += 1

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        amount = self.starting_Balance =+ amount
        balance = (f"The amount {amount} has been deposited in your account")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        try:
            balance = self.starting_Balance - amount
        except amount >= self.starting_Balance:
            raise ValueError("the transaction has been declined, Insufficient funds")
    def AccountDetails():
       return f"""
                    Your Account Details Here.
       """
Account1 = Account("Adam Ibrahim", "123456789", 0)

print(Account1.AccNo)
Account1.deposit()
print(Account1.starting_Balance)
print(Account.NoOfAccounts)


# ### This can be used as a repository?
# # Users
# adam = ATM("Adam Ibrahim", "123456789", 100, 321)
# eve = ATM("Eve Johnson", "987654321", 200, 123)
# john = ATM("John Doe", "111222333", 500, 999)

# # Store accounts in a dictionary by account number
# accounts = {
#     adam.AccNo: adam,
#     eve.AccNo: eve,
#     john.AccNo: john
# }

# -------------------------------------------------------------------------------------------------------------------------------