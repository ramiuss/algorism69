def nPr (n, r) :
    result = 1
    for i in range(n-r +1, n + 1) :
        result *= i
    return result

print(nPr(5, 3))    



def nCr (n, r) :
    result = 1
    for i in range(n - r + 1, n + 1) :
        result *= i
    for i in range(1, r + 1) :
        result //= i
    return result

print(nCr(5, 3))