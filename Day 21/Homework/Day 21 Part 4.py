
input_number = 41823712738912987312

def descending_order(input_number):
    sorted_digits = sorted(str(input_number), reverse=True)
    new_num = ''.join(sorted_digits)
    return int(new_num)

print(descending_order(input_number))