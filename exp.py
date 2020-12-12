# exponential function

import complex
import config

def exp(x, prec=config.prec):
    x = complex.Complex(x)
    res = complex.Complex(0)
    k = 0
    numerator = complex.Complex(1)
    divisor = 1
    while True:
        c = numerator / divisor
        res += c
        if k > x.abs() and c.abs() < prec:
            return res
        k += 1
        numerator *= x
        divisor *= k

if __name__ == "__main__":
    print(exp(1, prec=0.0001))
