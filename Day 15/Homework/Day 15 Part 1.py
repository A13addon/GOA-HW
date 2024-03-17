

num1 = int(input("Please enter an int: "))

if num1 % 2 == 0:
    print("Number is even!")

else:
    print("Number is odd!")
    print("Next closest even number is" + " "  + str(num1 + 1))