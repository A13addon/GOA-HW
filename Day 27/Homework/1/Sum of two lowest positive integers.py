#Code (Mostly) without inner functions:

numbers = [10, 343445353, 3453445, 3453545353453]
final_list = []

def remove_smallest_number(numbers):
    num = numbers[0]
    for char in numbers:
        if char < num:
            num = char
    return num

num = remove_smallest_number(numbers)
numbers.remove(num) 
final_list.append(num)

def remove_second_number(numbers):
    num1 = numbers[0]
    for char1 in numbers:
        if char1 < num1:
            num1 = char1
    return num1

num1 = remove_second_number (numbers)
final_list.append(num1)

print(sum(final_list))


#Code with inner functions:
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


    
