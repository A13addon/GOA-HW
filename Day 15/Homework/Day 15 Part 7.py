
user_number = int(input("Please enter the first int: "))
user_number1 = int(input("Please enter the second int: "))

user_operator = input("Please enter an operator (+, -, *, /, **) ")

if user_operator == '+' :
    print(user_number + user_number1)

if user_operator == '-' :
    print(user_number - user_number1)

if user_operator == '/' :
    print(user_number / user_number1)

if user_operator == '*' :
    print(user_number * user_number1)

if user_operator == '**' :
    print(user_number ** user_number1)

