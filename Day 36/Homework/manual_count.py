x = ([12, 13, 14, 12, 14, 100], 12)
count = 0

def manual_count(x):
    for num in x[0]:
        if num == x[1]:
            global count
            count += 1
    return count

print(manual_count(x))