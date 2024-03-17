
correct_letter = ['G', 'g']

while True:
    user_input1 = str(input("Please input valid string: "))
    if user_input1[0] in correct_letter:
        print("Your string is correct!")
        break

    else:
        print("Please try again.")

    