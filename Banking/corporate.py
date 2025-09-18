#[V1 corporate]
from acc import Account

class corporate(Account):
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

    def transfer(self, accounts):
        recipient_AccNo = input("Enter Account number:")

        if recipient_AccNo == self.AccNo:
            print("You cannot transfer to your own account.")
            return

        recipient = accounts.get(recipient_AccNo)

        if not recipient:
            print("Account not found.")
            return

        try:
            amount = int(input("Enter amount to transfer: "))
            if amount > self.starting_Balance:
                print("Insufficient funds.")
            else:
                self.starting_Balance -= amount
                recipient.starting_Balance += amount
                print(f"{amount} transferred. {recipient.AccName}")
                print(f"{amount} transferred. New balance: {self.starting_Balance}")
        except ValueError:
            print("Invalid amount.")

Adam = corporate("Adam Ibrahim", "123456789", 100, 321)

# --------------------------------------------------------------------------------------------

### This can be used as a repository?
# Users
adam = corporate("Adam Ibrahim", "123456789", 100, 321)
eve = corporate("Eve Johnson", "987654321", 200, 123)
john = corporate("John Doe", "111222333", 500, 999)

# Store accounts in a dictionary by account number
accounts = {
    adam.AccNo: adam,
    eve.AccNo: eve,
    john.AccNo: john
}

# ----------------------------------------------------------------------------------------------

if Adam.login():
    while True:
        action = input("Choose Action: Deposit [1], Withdraw [2], Transfer[3], Quit [4]: ")
        if action == '1':
            Adam.deposit()
        elif action == '2':
            Adam.withdraw()
        elif action == '3':
            Adam.transfer(accounts)
        elif action == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option.")
else:
    print("Access denied. Exiting program.")

