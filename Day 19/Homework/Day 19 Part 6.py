# Beginner - Lost without a Map


a = [1, 2, 3, 4, 5]
final = []

def maps(a):
    for num in a:
        final += (num * 2 for num in a)
        return final

print(maps(a))