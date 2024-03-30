# https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/train/python

def flick_switch(lst):
    s = True
    lst1 = []
    for i in lst:
        if i == 'flick':
            s = not s
        lst1.append(s)
        
    return lst1

# https://www.codewars.com/kata/5b853229cfde412a470000d0

def twice_as_old(dad_age, son_age):
    return abs(dad_age - 2*son_age)


# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

def count_sheep(n):
        a=''
        for i in range (1,n+1):
            a= a+ str(i) + ' sheep...'
            i+=1
        return a

# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/solutions

def is_uppercase (num):
    return num == num.upper()


# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e

num1 = str(input("Please enter a string: "))
num2 = int(input("Please enter an int: "))

def repeat_str(num1, num2):
    num = str(num2*num1)
    return num

print(repeat_str(num1, num2))