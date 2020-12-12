# binomial coefficient

def binom(a, b):
    p = 1
    for i in range(a - b + 1, a + 1):
        p *= i
    for i in range(1, b + 1):
        p //= i
    return p

