# n! = n * (n - 1) * (n - 2).... * 1
# nPr = n * (n - 1) * (n - 2) .... *(n - r + 1) 
# nCr = n! / r! * (n - r)! = nPr / r!

import time
start_time = time.time()

def factorial(n) :
    result = 1
    for i in range(1, n + 1) :
        result *= i 
    return result

print(factorial(5))
print(factorial(40))

end_time = time.time()
print(f'Execution time : {end_time - start_time}')


def nPr(n, r) :
    result = 1
    for i in range(n - r + 1, n + 1) :
        result *= i
    return result

print(nPr(5, 3))

def nCr(n, r) :
    result = 1 
    for i in range(n - r + 1, n + 1) :
        result *= i
    for j in range(1, r + 1) :
        result //= j
    return result

print(nCr(5, 3))

start_time = time.time()

memo = {}
memo[0] = 1
def factorial(n) :
    global memo
    if n in memo :
        return memo[n]
    memo[n] = n * factorial(n - 1)
    return memo[n]

print(factorial(5))
print(factorial(40))

end_time = time.time()
print(f'Execution time : {end_time - start_time}')