
string_list = ["Saba", "Misho", "Malxazi", "Giorgi", "Luka"]

def string_filter (string_list):
    return [num for num in string_list if len(num) >= 5]

print(string_filter(string_list))