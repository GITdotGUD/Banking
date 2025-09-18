import acc as Account

# ATM CHOOSE BANK
class BANK(Account):
    def __init__(self, AccName, AccNo, starting_Balance, pin, bank):
        super().__init__(AccName, AccNo, starting_Balance)
        self.pin = pin
        self.bank = bank

# Choose Bank
# Have to add if the user has those banks or no
    def choose_bank(self):
        bank = input("Choose Bank: BML [1], MIB [2], BOC [3]: ")
        if bank == '1':
            print("You have chosen BML")
        elif bank == '2':
            print("You have chosen MIB")
        elif bank == '3':
            print("You have chosen BOC")
        else:
            print("Invalid bank selection.")

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

BML_Acc = BANK("Adam Ibrahim", "123456789", 1000, 321, "BML")
MIB_Acc = BANK("Ali Hassan", "987654321", 1500, 123, "MIB")
BOC_Acc = BANK("Sara Ahmed", "111222333", 2000, 456, "BOC")

# -------------------------------------------------------------------------------------------------------------------------------
### This can be used as a repository?

# Create bank accounts
BML = BANK("Adam Ibrahim", "123456789", 1000, 321, "BML")
MIB = BANK("Ali Hassan", "987654321", 1500, 123, "MIB")
BOC = BANK("Sara Ahmed", "111222333", 2000, 456, "BOC")

# Store accounts in a dictionary by account number
Banks = {
    BML.AccNo: BML,
    MIB.AccNo: MIB,
    BOC.AccNo: BOC
}

# Store accounts in a dictionary by account number (used for login and transfer)
accounts = {
    BML_Acc.AccNo: BML_Acc,
    MIB_Acc.AccNo: MIB_Acc,
    BOC_Acc.AccNo: BOC_Acc
}

# Optional: also store by bank name if needed
Banks = {
    BML_Acc.bank: BML_Acc,
    MIB_Acc.bank: MIB_Acc,
    BOC_Acc.bank: BOC_Acc
}
# -------------------------------------------------------------------------------------------------------------------------------

user_acc_no = input("Enter your account number: ")
user = accounts.get(user_acc_no)

if not user:
    print("Account not found.")
else:
    if user.login():
        while True:
            user.choose_bank()
            # Needs more refining
            action = input("Choose Action: Deposit [1], Withdraw [2], Transfer [3], Quit [4]: ")
            if action == '1':
                user.deposit()
            elif action == '2':
                user.withdraw()
            elif action == '3':
                user.transfer(accounts)
            elif action == '4':
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid option.")
    else:
        print("Access denied. Exiting program.")
