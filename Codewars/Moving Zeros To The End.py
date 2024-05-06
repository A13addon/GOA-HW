def move_zeros(lst):
    final_list = []
    for number in lst:
        if number != 0:
            final_list.append(number)
    for number in lst:
        if number == 0:
            final_list.append(number)
    return final_list