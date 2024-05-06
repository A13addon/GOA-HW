def to_weird_case(words):
    s = words.split()
    result = []

    for word in s:
        upper_letters = ''

        for i in range(len(word)):
            if i % 2 == 0:
                upper_letters += word[i].upper()

            else:
                upper_letters += word[i].lower()
        result.append(upper_letters)

    return ' '.join(result)