

input_number = 91119

def square_every_digit(input_number):
    num_str = str(input_number)
    final = ''

    for digit in num_str:
        final_digit = str(int(digit) ** 2)
        final += final_digit
    
    return int(final)

print(square_every_digit(input_number))
