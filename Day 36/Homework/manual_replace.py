
x = ([10, 11, 10, 11], 10, 20 )
list = x[0]
final = []

def manual_replace (x):
    for item in list:
        if item == x[1]:
            final.append(x[2])
        else:
            final.append(item)

    return final

print(manual_replace(x))