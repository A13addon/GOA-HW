
sentence = "eg ariyo ritma"

def get_count(sentence):
    final_len = 0
    for num in sentence:
        if num == "a":
            final_len += len(num)
        if num == "e":
            final_len += len(num)
        if num == "i":
            final_len += len(num)
        if num == "o":
            final_len += len(num)
        if num == "u":
            final_len += len(num)


    return final_len

print(get_count(sentence))
