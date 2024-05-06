def variance(numbers): 
    mean = sum(numbers) / len(numbers)
    variance_alg = 0
    
    for number in numbers:
        variance_alg += (float(number) - mean)**2
    final_variance = variance_alg / len(numbers)
    return final_variance