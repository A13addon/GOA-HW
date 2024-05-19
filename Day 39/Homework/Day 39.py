################# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

# def duplicate_encode(word):
#     word = word.lower()  # Convert the string to lowercase
#     result = ""
#     for char in word:
#         if word.count(char) > 1:
#             result += ")"
#         else:
#             result += "("
#     return result

################## https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

# def is_pangram(s):
#     alphabet = set("abcdefghijklmnopqrstuvwxyz")
#     for char in s.lower(): 
#         if char.isalpha():
#             alphabet.discard(char)
#     return not alphabet

################### https://www.codewars.com/kata/59daf400beec9780a9000045/train/python

# def name_in_str(strng, name):
#     name_index = 0
#     for char in strng.lower():
#         if char == name[name_index].lower():
#             name_index += 1
#             if name_index == len(name):
#                 return True
#     return False 
            
################### https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

# def first_non_repeating_letter(s):
#     s_low = s.lower()
#     for i in s:
#         if s_low.count(i.lower()) == 1:
#             return i
#     return ""