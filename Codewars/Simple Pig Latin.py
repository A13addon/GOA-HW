def pig_it(text):
    ss = text.split()
    result = []
    for word in ss:
        if word.isalpha():
            final_add = word[0] + "ay"
            result.append(word[1:] + final_add )
        else:
            result.append(word)
    return ' '.join(result)