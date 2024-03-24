# Abbreviate a Two Word Name

def abbrev_name(name):
    words = name.split()
    initials = [word[0].upper() + '.' for word in words]
    return ''.join(initials)[:-1]

name = "Sam Harris"
print(abbrev_name(name))