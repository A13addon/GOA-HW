correct_password = "password123"

while True:
    user_password = input("Please enter your password:")

    if user_password == correct_password:
        print("Access granted! ")
        break
    
    else:
        print("Password is incorrect, please enter correct one. ")
    
