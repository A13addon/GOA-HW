def collatz(n):
    final = [str(n)]
    while n != 1 and n != 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        final.append(str(n))
    return '->'.join(final)
    