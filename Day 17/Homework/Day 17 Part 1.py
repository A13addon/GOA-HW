num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
num3 = [num1, num2]

number_list = [num for num in range(min(num3), max(num3))]

def sum_of_numbers (number_list):
    return sum(number_list)

print(sum_of_numbers(number_list))