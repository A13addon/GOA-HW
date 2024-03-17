
start_number = int(input("Please enter the starting number: "))
end_number = int(input("Please enter an ending number: "))
numbers = [start_number, end_number]
final_list = []

for i in range (min(numbers), max(numbers)):
    if i % 5 == 0:
        final_list.append(i)

print(final_list)

