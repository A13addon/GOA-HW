
final_output = 1

while True:
    num1 = int(input("Please enter an int: "))

    if num1 < 0:
        print("Factorial of negative numbers is not defined! ")
        break
    
    if num1 == 0:
        print("0! = 1")
        break
    else:
        for i in range (1, num1 + 1):
            final_output *= i
        print(final_output)