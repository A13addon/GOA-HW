# https://www.codewars.com/kata/5266fba01283974e720000fa

# numbers = [1, 2, 2, 3]
# def variance(numbers): 
#     mean = sum(numbers) / len(numbers)
#     variance_alg = 0
    
#     for number in numbers:
#         variance_alg += (float(number) - mean)**2
#     final_variance = variance_alg / len(numbers)
#     return final_variance

# print(variance(numbers))

########################
# https://www.codewars.com/kata/52449b062fb80683ec000024

# s = " Hello there thanks for trying my Kata"
# final_s = "#"

# def generate_hashtag(s):
#     if len(s) < 1 or len(s) > 140:
#         return False
    
#     for word in s:
#         s_sp = s.split()
    
#     for word in s_sp:
#         global final_s
#         final_s += word.capitalize()
#     return final_s

# print(generate_hashtag(s))

########################################

# https://www.codewars.com/kata/52597aa56021e91c93000cb0

# lst = [1, 0, 1, 2, 0, 1, 3]


# def move_zeros(lst):
#     final_list = []
#     zero = 0
#     for number in lst:
#         if number != 0:
#             final_list.append(number)
    
#     for number in lst:
#         if number == 0:
#             final_list.append(number)
#     return final_list

# print(move_zeros(lst))

#############################

# https://www.codewars.com/kata/520b9d2ad5c005041100000f

# text = 'Pig latin is cool'

# def pig_it(text):
#     ss = text.split()
#     result = []
#     for word in ss:
#         if word.isalpha():
#             final_add = word[0] + "ay"
#             result.append(word[1:] + final_add )
#         else:
#             result.append(word)
#     return ' '.join(result)

################################