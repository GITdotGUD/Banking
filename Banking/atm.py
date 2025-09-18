#[V2]
from acc import Account


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