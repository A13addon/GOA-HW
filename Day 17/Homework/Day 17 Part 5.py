
name_list = ["Amirani", "Ana", "Anastasia", "Misho", "Luka", "Giorgi", "Malxazi", "Nika"]

def name_sorter (name_list):
    return [num for num in name_list if num[0:1] == "A"]

print(name_sorter(name_list))