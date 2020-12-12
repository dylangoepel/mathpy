# trigonometric functions

import exp
from complex import Complex

sin = lambda x: exp.exp(Complex(0, x)).imag
cos = lambda x: exp.exp(Complex(0, x)).real

tan = lambda x: sin(x) / cos(x)
