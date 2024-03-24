# Calculate average


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def find_average(numbers):
    sum = 0
    for num in numbers:
        sum += num
    average = sum / len(numbers)
    return average

print(find_average(numbers))