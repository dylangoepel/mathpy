# approximation of pi using trigonometric functions

from trigon import cos
from num import solve
import config

def pi(prec=config.prec):
    return solve(cos, prec=prec / 2) * 2

if __name__ == "__main__":
    print(pi())
