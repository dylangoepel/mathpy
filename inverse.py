# numerically approximate inverse functions

import num
import config

def inverse(f):
    return lambda y: num.solve(lambda x: f(x) - y, prec=config.prec)
