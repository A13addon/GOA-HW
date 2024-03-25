
weight = int(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))


def bmi(weight, height):
    if weight / height ** 2 <= 18.5:
        return "Underweight"
    
    if weight / height ** 2 <= 25.0:
        return "Normal"
    
    if weight / height ** 2 <= 30.0:
        return "Overweight"
    
    if weight / height ** 2 > 30:
        return "Obese"
    
    
print(bmi(weight, height))

    