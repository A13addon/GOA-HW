
correct_password = "abc123"

while True:
    user_password = input("Please enter a password: ")
    if user_password == correct_password:
        print("Access Granted! ")
        break
    while user_password != correct_password:
        second_try = input("Password is incorrect, please try again: ")

    if second_try == correct_password:
        print("Access Granted! ")
        break