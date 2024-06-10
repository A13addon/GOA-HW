# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])

# კოდი ზრდადობით ალაგებს სიას და ბოლოს კრებს დალაგებული სიის პირველ ორ, ანუ ყველაზე მცირე რიცხვებს

# https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python



# def max_multiple(divisor, bound):
#     list = []
#     for i in range(0, bound+1):
#         if i % divisor == 0:
#             list.append(i)

#     return max(list)

# კოდი ქმნის for ციკლს ნულიდან bound-ის ჩათვლით და შემდგომ პირობის დაკმაყოფილების შემთხვევაში ამატებს list-ში. ბოლოს აბრუნებს list-ში დამატებულ უდიდეს რიცხვს.

# https://www.codewars.com/kata/514a6336889283a3d2000001/train/python

# def get_even_numbers(arr):
#     final = []
#     for i in arr:
#         if i % 2 == 0:
#             final.append(i)
#     return final

# კოდი ქმნის სიმრავლეს სახელად final, რომელშიც ემატება მხოლოდ ისეთი რიცხვები, რომლებიც 2-ზე უნაშთოდ იყოფიან. კოდის ბოლოს ეს სიმრავლე ბრუნდება.


# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9


# def row_weights(array):
#     fr = 0
#     sr = 0
#     for index, i in enumerate(array):
#         if index % 2 == 0:
#             fr += i
#         else:
#             sr += i
#     final = (fr, sr)
#     return final


# კოდი ქმნის 2 ცვლადს, შემდგომ ქმნის ციკლს array მასივში ნუმერაციისთვის, რომელსაც ერქმევა index. შემდგომ თუ ინდექსი იყოფა 2-ზე უნაშთოდ, მაშინ იგი დაემატება პირველ ცვლადს, თუ არ იყოფა დაემატება მეორე ცვლადს. საბოლოოდ დაბრუნდება final, რომელიც პირველ და მეორე ცვლადებს მოიცავს.