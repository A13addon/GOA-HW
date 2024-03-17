

number_list = [1,2,3,4,5,6,7,8,9,10,11,21,22,3344,556,223,123,567,23123,42]

final_list = [num for num in number_list if num > 10]

def sum_of_number (final_list):
    return sum(final_list)


print(sum_of_number(final_list))