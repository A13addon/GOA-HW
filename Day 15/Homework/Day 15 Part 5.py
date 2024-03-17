

num1 = int(input("Please enter an integer: "))

for i in range(2, int(num1**0.5) + 1):
    if num1  % i == 0:
        print("Number is not prime! ")
        break
    
if num1 <= 1:
    print("Number is not prime! ")

else:
    print("Number is prime! ")