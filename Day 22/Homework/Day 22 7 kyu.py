# https://www.codewars.com/kata/55a710b462afc49a540000b9/train/python

x = 69
def corrections(x):
    
    if x > 0: 
        return (str(x) + " is more than zero.")
    
    else:
        return (str(x) + " is equal to or less than zero.")
    

print(corrections(x))

# https://www.codewars.com/kata/5a4ff3c5fd56cbaf9800003e/train/python

def without_last(lst):
    
    lst.pop() 
    return lst

# https://www.codewars.com/kata/5a043724ffe75fbab000009f/train/python

def reverse_middle(lst):
    l = len(lst) // 2
    return lst[l-1:-l+1:][::-1]

# https://www.codewars.com/kata/5a6d3bd238f80014a2000187/train/python

def owned_cat_and_dog(cat_years, dog_years):
    i = cat_years
    k = dog_years
    if i < 24:
      cat_years = 1
    if k < 24:
      dog_years = 1
    if i == 24:
      cat_years = 2
    if k == 24:
      dog_years = 2
    if i > 24:
      cat_years = int((i - 24) / 4) + 2
    if k > 24:
      dog_years = int((k - 24) / 5) + 2
    if i < 15:
        cat_years = 0
    if k < 15:
        dog_years = 0
    return [cat_years, dog_years]

# https://www.codewars.com/kata/586e1d458cb711f0a800033b/solutions

def process_data(data):
    final = 1
    for sublist in data:
        final *= sublist[0] - sublist[1]
    return final