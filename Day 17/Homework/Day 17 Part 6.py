
number_list = [1,2,3,4,5,6,7,8,9,10,20,30,40,50]
squared_list = []

def square_calc (number_list):
    return [num ** 2 for num in number_list]

print(square_calc(number_list))

