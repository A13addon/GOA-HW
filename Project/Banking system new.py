import random

# Chad Banking System

accounts = {
     'account_balance': 0
      }
accounts['account_number'] = 'account_balance'

def main_func():
    while True:
        print("1. Create an account")
        print("2. Deposit funds")
        print("3. Withdraw funds")
        print("4. Check Balance")
        print("5. Exit")
        user_input = int(input("Please choose the operation: "))

        if user_input == 1:
            create_an_account(user_input)
        elif user_input == 2:
            deposit(user_input)
        elif user_input == 3:
            withdrawal(user_input)
        elif user_input == 4:
            check_balance(user_input)
        elif user_input == 5:
            exit(user_input)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

def create_an_account (user_input):
    user_name = input("Please enter your name: ")
    account_number = random.randint(10000000, 99999999)
    accounts['user_number'] = account_number
    print("You account number is " + str(account_number))
    account_balance = 0
    accounts['user_balance'] = account_balance
    print("Your account balance is " + str(account_balance))
    
    



def deposit (user_input):
    account_number = int(input("Please enter your account number: "))
    accounts['account_number'] = account_number
    
    while True:
        if account_number == accounts['account_number']:
                deposit_amount = int(input("Please enter the deposit amount: "))
                if deposit_amount > 0:
                    accounts['account_balance'] += deposit_amount
                    print("Successfully deposited " + str(deposit_amount))
                    break
                else:
                    deposit_amount_secondary = int(input("Please enter a valid amount: "))
                    accounts['account_balance'] += deposit_amount_secondary
                    print("Successfully deposited " + str(deposit_amount_secondary))
                    break
        
            

def withdrawal (user_input):
    account_number = int(input("Please enter your account number: "))
    if account_number == accounts['account_number']:
        withdrawal_amount = int(input("Please enter withdrawal amount: "))
        if withdrawal_amount <= accounts['account_balance']:
            accounts['account_balance'] = accounts['account_balance'] - withdrawal_amount
            print(str(withdrawal_amount) + " Has been successfully withdrawn from your account. There is " + str(accounts["account_balance"]) + " left")
        if accounts["account_balance"] == 0:
            print("There are no credits to withdraw!")
        else:
            print("Value exceeds the account balance")
            withdrawal_amount_secondary = int(input("Please enter a valid amount: "))
            accounts['account_balance'] = accounts['account_balance'] - withdrawal_amount_secondary
            print(str(withdrawal_amount_secondary) + " Has been successfully withdrawn from your account.")
    else:
        print("Account number is incorrect! ")
        create_an_account(user_input)


def check_balance (user_input):
    account_number = int(input("Please enter your account number: "))
    if account_number == accounts['account_number']:
        print("Your account balance is " + str(accounts["account_balance"]))


def exit (user_input):
    while True:
        if user_input == 5:
            break




main_func()