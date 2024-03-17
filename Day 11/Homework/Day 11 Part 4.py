while True:
    
    atm_pin = (input("Please enter your PIN: "))
    correct_pin = "1234"
    if len(atm_pin) <= 4:
        num1 = int(atm_pin)

    else:
        print("Invalid PIN, please enter a valid PIN: ")

    
    if atm_pin == correct_pin:
        print("Pin is correct, you can proceed! ")

        print("Withdrawal, Deposit or Balance? ")
        break
    
    else:
        print("PIN is incorrect, please tty again")
