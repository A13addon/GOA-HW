number_list = []
for i in range (100):
    number_list.append(i)

def even_filter (number_list):
    return [num for num in number_list if num % 2 == 0]

print(even_filter(number_list))