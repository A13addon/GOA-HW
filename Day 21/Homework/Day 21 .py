
arr = [1, 2, 3, 4]

def grow(arr):
    final = 1
    for num in arr:
        final *= num 

    return final

print(grow(arr))
