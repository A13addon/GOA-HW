

num1 = int(input("Please enter the quantity of list numbers: "))

def sum_of_numbers (list_of_numbers):
    for num in range(num1):
        number_list = []
        num2 = int(input("Please add a number: "))
        number_list.append(num2)
        number_list = number_list + num
        print(number_list)

print(sum_of_numbers)