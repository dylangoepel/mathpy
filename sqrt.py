# square roots of real numbers

import config
import num

def sqrt(x, prec=config.prec):
    if x < 0:
        raise ValueError("negative radicand")

    return num.solve(lambda c: c * c - x, prec=prec)

# approximate sqrt(2)
if __name__ == "__main__":
    print(sqrt(2))
