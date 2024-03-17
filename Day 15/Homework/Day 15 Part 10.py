
num1 = int(input("Please enter a whole number: "))

if num1 >= 0:
    factorial_result = 1


    for i in range(1, num1 + 1):
        factorial_result *= i


print(factorial_result)