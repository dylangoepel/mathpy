# find roots of a function numerically

import config

def _sig(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

# finds the first root of f in the interval [0, +infty)
def solve(f, prec=config.prec):
    c = 0
    step = 1
    oval = f(0)
    osig = _sig(oval)
    while step > prec:
        val = f(c)
        if val == 0:
            return c
        elif _sig(val) != osig:
            c -= step
            step = step / 10
        c += step
    return c
