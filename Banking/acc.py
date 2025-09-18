# make subclasses for ATM and Account
# make a login function for ATM
# make a deposit and withdraw function for ATM
# make a function to display account details for Account
# make it so that there are saving subclaases which you u can view
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

#[V2]
class ATM(Account):
    def __init__(self, AccName, AccNo, starting_Balance, pin):
        super().__init__(AccName, AccNo, starting_Balance)
        self.pin = pin

#login to the account

    def login(self):
        attempts = 0

        while attempts < 3:
            entered_pin = int(input("Enter PIN: "))

            if entered_pin == self.pin:
                print("Access granted.")
                return True
            else:
                print("Incorrect PIN.")
                attempts += 1

        print("Too many failed attempts. Access denied.")
        return False

#load the Account functions

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.starting_Balance += amount
        print(f"The amount {amount} has been deposited in your account. New balance: {self.starting_Balance}")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.starting_Balance:
            print("The transaction has been declined, insufficient funds.")
        else:
            self.starting_Balance -= amount
            print(f"The amount {amount} has been withdrawn from your account. New balance: {self.starting_Balance}")

#This needs more thingys, it dont feel right

Adam = ATM("Adam Ibrahim", "123456789", 100, 321)

if Adam.login():
    while True:
        action = input("Choose Action: Deposit [1], Withdraw [2], Quit [3]: ")
        if action == '1':
            Adam.deposit()
        elif action == '2':
            Adam.withdraw()
        elif action == '3':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option.")
else:
    print("Access denied. Exiting program.")


# -------------------------------------------------------------------------------------------------------------------------------

