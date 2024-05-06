def array_diff(a, b):
    final_list = []
    
    for number in a:
        if number not in b:
            final_list.append(number)
    return final_list