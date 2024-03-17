

while True:
    user_input = (input("Please enter an int: "))
    if type(user_input) == int:

        if int(user_input) > 0:
            print("Integer is positive!")
            break

        if int(user_input) == 0:
            print("Integer is a zero!")
            break

        if int(user_input) < 0:
            print("Integer is negative! ")
            break

    else: 
        print("Please input valid int")
        