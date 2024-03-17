
correct_password = "Goa is best"
incorrect_tries = 0

while True:
        num1 = input("Please enter your password: ")
        if num1 == correct_password:
            print("Access granted!")
            break
        else:
            incorrect_tries += 1
            print("Password is incorrect! Please try again: ")
            print("You have " + str(incorrect_tries) + " tries")
            
      