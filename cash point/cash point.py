class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


user = BankAccount('Smith')

amount = 0.0
while True:
    money = int(input("What would you like to do?\n   1)withdraw\n   2)deposit\n   3)EXIT?\n "))
    if money == 1:
        money_withdraw = int(input('How much do you want to take? '))
        total = amount - money_withdraw
        print(total)
        print(f"You withdraw {money_withdraw}£ your sold is {total}£")
        continue_operation = input("Would you like to continue? type 'y' for yes and 'n' for no:")
        if continue_operation == 'y':
            continue
        elif continue_operation == 'n':
            break
        else:
            print("Choose 'y' or 'n' ")
    elif money == 2:
        money_deposit = int(input('How much would you like to deposit? '))
        total = amount + money_deposit
        print(f"You deposited {money_deposit}£ your sold is {total}£")
    elif money == 3:
        print('Thanks!!! See you next time.')
        break
    else:
        print("Select the correct option: 1, 2 or 3")