# complex numbers

from sqrt import sqrt

class Complex:
    def __init__(self, *args):
        if len(args) == 1:
            if type(args[0]) == Complex:
                self.real, self.imag = args[0].real, args[0].imag
            else:
                self.real, self.imag = args[0], 0
        elif len(args) == 2:
            self.real, self.imag = args[0], args[1]
        else:
            raise ValueError()

    def abs(self):
        return sqrt(self.real * self.real) + sqrt(self.imag * self.imag)

    def __add__(self, other):
        if type(other) == Complex:
            return Complex(self.real + other.real, self.imag + other.imag)
        else:
            return Complex(self.real + other, self.imag)

    def __mul__(self, other):
        if type(other) == Complex:
            return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
        else:
            return Complex(other * self.real, other * self.imag)

    def __str__(self):
        return "{} + {} * i".format(self.real, self.imag)

    def __truediv__(self, other):
        if type(other) == Complex:
            divisor = other.real * other.real + other.imag * other.imag
            return Complex((self.real * other.real + self.imag * other.imag) / divisor, (other.real * self.imag - self.real * other.imag) / divisor)
        else:
            return Complex(self.real / other, self.imag / other)
